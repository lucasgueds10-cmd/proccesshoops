import { NextResponse } from "next/server";

export const dynamic = "force-dynamic";
export const maxDuration = 10;

// Rota temporária de diagnóstico: testa se a rede de execução da Vercel
// consegue falar com stats.nba.com. Será removida após o teste.
export async function GET() {
  const target =
    "https://stats.nba.com/stats/leaguestandingsv3?LeagueID=00&Season=2025-26&SeasonType=Regular%20Season";

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 8000);
  const startedAt = Date.now();

  try {
    const res = await fetch(target, {
      signal: controller.signal,
      headers: {
        Accept: "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent":
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        Referer: "https://www.nba.com/",
      },
    });
    const elapsedMs = Date.now() - startedAt;
    const bodyPreview = (await res.text()).slice(0, 200);
    return NextResponse.json({ ok: res.ok, status: res.status, elapsedMs, bodyPreview });
  } catch (error) {
    const elapsedMs = Date.now() - startedAt;
    return NextResponse.json(
      { ok: false, elapsedMs, error: error instanceof Error ? error.message : String(error) },
      { status: 502 },
    );
  } finally {
    clearTimeout(timeout);
  }
}
