"use client";

import React from "react";
import { motion } from "framer-motion";

export default function StatusPage() {
    return (
        <div style={{ minHeight: "100vh", display: "flex", flexDirection: "column", background: "var(--bg-main)", color: "var(--text-primary)" }}>
            <nav className="navbar">
                <div className="container" style={{ maxWidth: "800px" }}>
                    <a href="/" className="nav-logo">
                        <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
                            <path d="M12 2L2 22h20L12 2z"></path>
                        </svg>
                        CloudMeld
                    </a>
                    <ul className="nav-links">
                        <li><a href="/security">Security</a></li>
                        <li><a href="/status" style={{ color: "var(--text-primary)" }}>System Status</a></li>
                    </ul>
                </div>
            </nav>

            <main style={{ flex: 1, display: "flex", alignItems: "center", justifyContent: "center", padding: "2rem" }}>
                <motion.div
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 0.5, ease: "easeOut" }}
                    style={{
                        background: "var(--bg-surface)",
                        border: "1px solid var(--border-color)",
                        borderRadius: "var(--radius-xl)",
                        padding: "3rem",
                        width: "100%",
                        maxWidth: "500px",
                        boxShadow: "0 20px 40px rgba(0,0,0,0.5)"
                    }}
                >
                    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", borderBottom: "1px solid var(--border-color)", paddingBottom: "1.5rem", marginBottom: "1.5rem" }}>
                        <h1 style={{ fontSize: "1.25rem", fontWeight: 600, letterSpacing: "-0.02em" }}>Infrastructure Status</h1>
                        <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", fontSize: "0.875rem", fontWeight: 500, color: "#10b981", background: "rgba(16, 185, 129, 0.1)", padding: "0.25rem 0.75rem", borderRadius: "20px" }}>
                            <span
                                style={{
                                    width: "8px",
                                    height: "8px",
                                    borderRadius: "50%",
                                    backgroundColor: "#10b981",
                                    display: "inline-block",
                                    boxShadow: "0 0 8px rgba(16, 185, 129, 0.8)"
                                }}
                            />
                            Operational
                        </div>
                    </div>

                    <div style={{ display: "flex", flexDirection: "column", gap: "1.25rem" }}>
                        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                            <span style={{ color: "var(--text-secondary)", fontSize: "0.875rem" }}>Global Environment</span>
                            <span style={{ fontSize: "0.875rem", fontWeight: 500, color: "var(--text-primary)" }}>Online</span>
                        </div>
                        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                            <span style={{ color: "var(--text-secondary)", fontSize: "0.875rem" }}>Uptime SLA</span>
                            <span style={{ fontSize: "0.875rem", fontWeight: 500, color: "var(--text-primary)" }}>99.99%</span>
                        </div>
                        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                            <span style={{ color: "var(--text-secondary)", fontSize: "0.875rem" }}>Deployment Layer</span>
                            <span style={{ fontSize: "0.875rem", fontWeight: 500, color: "var(--text-primary)" }}>Ready</span>
                        </div>
                        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                            <span style={{ color: "var(--text-secondary)", fontSize: "0.875rem" }}>Edge Routing</span>
                            <span style={{ fontSize: "0.875rem", fontWeight: 500, color: "var(--text-primary)" }}>Healthy</span>
                        </div>

                        <div style={{ marginTop: "1rem", paddingTop: "1.5rem", borderTop: "1px dashed var(--border-color)" }}>
                            <p style={{ fontSize: "0.8125rem", color: "var(--text-secondary)", margin: 0 }}>
                                <strong style={{ color: "var(--text-muted)", fontWeight: 500, marginRight: "0.5rem" }}>Last Incident:</strong>
                                None reported in the last 90 days.
                            </p>
                        </div>
                    </div>
                </motion.div>
            </main>

            <footer className="footer" style={{ borderTop: "none", background: "transparent", padding: "2rem 0" }}>
                <div className="container" style={{ maxWidth: "800px" }}>
                    <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textAlign: "center", borderTop: "1px solid var(--border-color)", paddingTop: "1.5rem" }}>
                        Systems automatically monitored 24/7/365. All datacenters operating nominally.
                    </div>
                </div>
            </footer>
        </div>
    );
}
