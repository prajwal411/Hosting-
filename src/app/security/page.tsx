"use client";

import React from "react";
import { motion } from "framer-motion";

const SECURITY_SECTIONS = [
    {
        title: "Data Protection",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        ),
        features: [
            { name: "Encrypted Traffic", desc: "All connections are enforced to use HTTPS over TLS 1.3 by default, ensuring transit-layer data encryption." },
            { name: "TLS Certification", desc: "Automated provisioning and real-time renewal of secure socket layer certificates across global deployment edges." },
            { name: "Secure DNS Routing", desc: "Protective DNS delegation preventing cache poisoning and mitigating massive-scale distributed denial-of-service vectors." }
        ]
    },
    {
        title: "Infrastructure Reliability",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        ),
        features: [
            { name: "99.9% Uptime SLA", desc: "Financially backed service level agreements engineered for continuous production environment availability." },
            { name: "Atomic Deployments", desc: "Immutable deployment model guaranteeing zero-downtime releases and rapid rollback capabilities." },
            { name: "Real-time Monitoring", desc: "Comprehensive system telemetry evaluating node health, anomalous traffic spikes, and localized edge degradation." }
        ]
    },
    {
        title: "Billing & Compliance",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
        ),
        features: [
            { name: "GST Compliance", desc: "Standardized invoicing structures incorporating valid GSTIN tracking for enterprise tax reporting operations." },
            { name: "Secure Payment Provisioning", desc: "Payment pathways strictly routed through Razorpay, a PCI-DSS certified financial handling infrastructure." },
            { name: "Transparent Pricing", desc: "Deterministic cost models utilizing one-time infrastructure provision fees, eliminating unpredictable recurring overheads." }
        ]
    }
];

export default function SecurityPage() {
    return (
        <>
            <nav className="navbar">
                <div className="container">
                    <a href="/" className="nav-logo">
                        <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
                            <path d="M12 2L2 22h20L12 2z"></path>
                        </svg>
                        CloudMeld
                    </a>
                    <ul className="nav-links">
                        <li><a href="/#infrastructure">Infrastructure</a></li>
                        <li><a href="/#workflow">Workflow</a></li>
                        <li><a href="/security" style={{ color: "var(--text-primary)" }}>Security</a></li>
                    </ul>
                    <div className="nav-actions">
                        <a href="/#pricing" className="btn btn-secondary">Platform Access</a>
                    </div>
                </div>
            </nav>

            <main>
                <section className="hero" style={{ padding: "8rem 0 4rem", background: "none" }}>
                    <div className="container" style={{ textAlign: "left", maxWidth: "800px" }}>
                        <h1 className="hero-title" style={{ fontSize: "3rem", marginBottom: "1rem", textAlign: "left" }}>Platform Security</h1>
                        <p className="hero-subtitle" style={{ fontSize: "1.125rem", marginLeft: 0, textAlign: "left", maxWidth: "100%" }}>
                            Comprehensive technical specifications regarding infrastructure compliance, data protection, and deployment lifecycle security.
                        </p>
                    </div>
                </section>

                <section className="section no-border" style={{ paddingTop: 0 }}>
                    <div className="container" style={{ maxWidth: "800px" }}>
                        <div style={{ display: "flex", flexDirection: "column", gap: "4rem" }}>
                            {SECURITY_SECTIONS.map((section, idx) => (
                                <motion.div
                                    key={idx}
                                    initial={{ opacity: 0, y: 20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ duration: 0.5, delay: idx * 0.15 }}
                                    style={{ borderTop: "1px solid var(--border-color)", paddingTop: "3rem" }}
                                >
                                    <div style={{ display: "flex", alignItems: "center", gap: "1rem", marginBottom: "2rem" }}>
                                        <div style={{ color: "var(--text-primary)", width: "24px", height: "24px" }}>
                                            {section.icon}
                                        </div>
                                        <h2 style={{ fontSize: "1.5rem", fontWeight: 600, color: "var(--text-primary)" }}>
                                            {section.title}
                                        </h2>
                                    </div>

                                    <div style={{ display: "flex", flexDirection: "column", gap: "2rem" }}>
                                        {section.features.map((feature, fIdx) => (
                                            <div key={fIdx}>
                                                <h3 style={{ fontSize: "1rem", fontWeight: 600, color: "var(--text-primary)", marginBottom: "0.5rem" }}>
                                                    {feature.name}
                                                </h3>
                                                <p style={{ fontSize: "0.9375rem", color: "var(--text-secondary)", lineHeight: 1.6 }}>
                                                    {feature.desc}
                                                </p>
                                            </div>
                                        ))}
                                    </div>
                                </motion.div>
                            ))}
                        </div>
                    </div>
                </section>
            </main>

            <footer className="footer" style={{ marginTop: "4rem" }}>
                <div className="container">
                    <div className="footer-bottom" style={{ borderTop: "none", paddingTop: 0 }}>
                        <span>© {new Date().getFullYear()} CloudMeld Hosting. Infrastructure Security Division.</span>
                        <div style={{ display: "flex", gap: "1rem" }}>
                            <a href="/">Return to Platform</a>
                        </div>
                    </div>
                </div>
            </footer>
        </>
    );
}
