"use client";
import { useState } from "react";

export default function Home() {
  const [objective, setObjective] = useState("");
  const [krs, setKrs] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  async function generate() {
    setLoading(true);
    const res = await fetch("/api/ai/generate-kr", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ objective }),
    });
    const data = await res.json();
    setKrs(data.key_results || []);
    setLoading(false);
  }

  return (
    <main className="p-10 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">OKR Tracker AI</h1>
      <textarea
        value={objective}
        onChange={(e) => setObjective(e.target.value)}
        placeholder="Например: Увеличить MRR на 40% за Q1"
        className="w-full border p-3 rounded mb-4"
        rows={3}
      />
      <button
        onClick={generate}
        disabled={loading}
        className="bg-black text-white px-6 py-2 rounded"
      >
        {loading ? "Генерация..." : "Сгенерировать KR"}
      </button>
      <ul className="mt-6 space-y-2">
        {krs.map((kr, i) => (
          <li key={i} className="border-l-4 border-blue-500 pl-3">{kr}</li>
        ))}
      </ul>
    </main>
  );
}
