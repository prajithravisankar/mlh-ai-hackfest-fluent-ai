"use client";

import { useEffect, useRef, useCallback } from "react";

interface WaveformVisualizerProps {
  isActive: boolean;
  audioStream?: MediaStream | null;
  variant?: "default" | "compact";
}

export default function WaveformVisualizer({
  isActive,
  audioStream,
  variant = "default",
}: WaveformVisualizerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const animRef = useRef<number>(0);
  const analyzerRef = useRef<AnalyserNode | null>(null);
  const dataRef = useRef<Uint8Array<ArrayBuffer> | null>(null);

  // Set up Web Audio API analyzer if we have a real stream
  useEffect(() => {
    if (!audioStream || !isActive) {
      analyzerRef.current = null;
      dataRef.current = null;
      return;
    }

    try {
      const audioCtx = new AudioContext();
      const source = audioCtx.createMediaStreamSource(audioStream);
      const analyzer = audioCtx.createAnalyser();
      analyzer.fftSize = 128;
      analyzer.smoothingTimeConstant = 0.8;
      source.connect(analyzer);

      analyzerRef.current = analyzer;
      dataRef.current = new Uint8Array(analyzer.frequencyBinCount);

      return () => {
        source.disconnect();
        audioCtx.close();
        analyzerRef.current = null;
        dataRef.current = null;
      };
    } catch {
      // Web Audio not available, fall back to simulated
    }
  }, [audioStream, isActive]);

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const bars = variant === "compact" ? 24 : 40;
    const barWidth = canvas.width / bars;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < bars; i++) {
      let height: number;

      if (analyzerRef.current && dataRef.current) {
        // Real audio data
        analyzerRef.current.getByteFrequencyData(dataRef.current);
        const index = Math.floor((i / bars) * dataRef.current.length);
        height = (dataRef.current[index] / 255) * (canvas.height * 0.85) + 3;
      } else {
        // Simulated waveform
        const t = Date.now() / 200;
        height = Math.abs(Math.sin(t + i * 0.3)) * 30 + Math.random() * 10 + 4;
      }

      const x = i * barWidth + barWidth * 0.2;
      const w = barWidth * 0.6;
      const y = (canvas.height - height) / 2;

      const gradient = ctx.createLinearGradient(x, y, x, y + height);
      gradient.addColorStop(0, "#818cf8");
      gradient.addColorStop(1, "#6366f1");
      ctx.fillStyle = gradient;

      ctx.beginPath();
      ctx.roundRect(x, y, w, height, 2);
      ctx.fill();
    }

    animRef.current = requestAnimationFrame(draw);
  }, [variant]);

  useEffect(() => {
    if (!isActive) {
      cancelAnimationFrame(animRef.current);
      return;
    }
    draw();
    return () => cancelAnimationFrame(animRef.current);
  }, [isActive, draw]);

  if (!isActive) return null;

  const width = variant === "compact" ? 200 : 320;
  const height = variant === "compact" ? 40 : 64;

  return (
    <canvas
      ref={canvasRef}
      width={width}
      height={height}
      className="rounded-lg opacity-80"
    />
  );
}
