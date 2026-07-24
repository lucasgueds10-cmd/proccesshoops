import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Garante que os JSONs gerados pelo pipeline (fora de src/) sejam
  // incluídos no deploy da Vercel, já que são lidos via filesystem.
  outputFileTracingIncludes: {
    "/": ["./data/**/*"],
  },
};

export default nextConfig;
