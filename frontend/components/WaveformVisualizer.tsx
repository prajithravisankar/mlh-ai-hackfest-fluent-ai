"use client";

import { useEffect, useRef } from "react";

interface WaveformVisualizerProps {
  isActive: boolean;
}

export default function WaveformVisualizer({ isActive }: WaveformVisualizerProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const animRef = useRef<number>(0);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas || !isActive) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const bars = 40;
    const barWidth = canvas.width / bars;

    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      for (let i = 0; i < bars; i++) {
        // Simulate audio waveform with sine + randomness
        const t = Date.now() / 200;
        const height =
          Math.abs(Math.sin(t + i * 0.3)) * 30 +
          Math.random() * 10 +
          4;

        const x = i * barWidth + barWidth * 0.2;
        const w = barWidth * 0.6;
        const y = (canvas.height - height) / 2;

        // Gradient from accent to accent-light
        const gradient = ctx.createLinearGradient(x, y, x, y + height);
        gradient.addColorStop(0, "#818cf8");
        gradient.addColorStop(1, "#6366f1");
        ctx.fillStyle = gradient;

        ctx.beginPath();
        ctx.roundRect(x, y, w, height, 2);
        ctx.fill();
      }

      animRef.current = requestAnimationFrame(draw);
    };

    draw();

    return () => cancelAnimationFrame(animRef.current);
  }, [isActive]);

  if (!isActive) return null;

  return (
    <canvas
      ref={canvasRef}
      width={320}
      height={64}
      className="rounded-lg opacity-80"
    />
  );
}
