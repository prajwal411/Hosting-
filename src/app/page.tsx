"use client";

import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";

// Types
interface Plan {
    id: string;
    name: string;
    price: number;
    gst: number;
    total: number;
    desc: string;
    features: string[];
    popular?: boolean;
    buttonText: string;
}

// Data
const PLANS: Plan[] = [
    {
        id: "starter",
        name: "Starter Infrastructure",
        desc: "Ideal for single application deployments with standard traffic.",
        price: 7000,
        gst: 1260,
        total: 8260,
        features: [
            "Lifetime Hosting Access",
            "1 Production Deployment",
            "Global Edge Network",
            "Automated SSL Provisioning",
            "Basic Infrastructure Monitoring",
            "Standard SLA Support",
        ],
        buttonText: "Deploy Starter",
    },
    {
        id: "business",
        name: "Business Infrastructure",
        desc: "Optimized for scaling businesses requiring higher availability.",
        price: 18000,
        gst: 3240,
        total: 21240,
        features: [
            "Lifetime Hosting Access",
            "Up to 3 Production Deployments",
            "Priority Edge Routing",
            "Advanced Uptime Monitoring",
            "Performance Tuning",
            "Priority SLA Support",
        ],
        popular: true,
        buttonText: "Deploy Business",
    },
    {
        id: "enterprise",
        name: "Enterprise Infrastructure",
        desc: "Custom architecture for mission-critical enterprise workloads.",
        price: 35000,
        gst: 6300,
        total: 41300,
        features: [
            "Lifetime Hosting Access",
            "Unlimited Deployments",
            "Dedicated Infrastructure Setup",
            "Custom Security Configurations",
            "99.99% Guaranteed SLA",
            "Direct Technical Consultation",
        ],
        buttonText: "Request Enterprise Quote",
    },
];

const INFRASTRUCTURE_FEATURES = [
    {
        title: "Edge Network Deployment",
        desc: "Global edge distribution reducing latency worldwide.",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
        ),
    },
    {
        title: "Automated Global SSL",
        desc: "Zero-configuration TLS provisioning across all deployments.",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        ),
    },
    {
        title: "Zero Downtime Deployments",
        desc: "Atomic releases ensuring uninterrupted availability.",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
        ),
    },
    {
        title: "99.9% Uptime SLA",
        desc: "Enterprise-backed reliability guarantees.",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        ),
    },
    {
        title: "Secure DNS Routing",
        desc: "Advanced routing protection against DDoS vectors.",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        ),
    },
    {
        title: "Continuous Monitoring",
        desc: "Real-time infrastructure health tracking and alerting.",
        icon: (
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
        ),
    },
];

const ARCHITECTURE_STEPS = [
    { title: "Client", desc: "Origin requests from user endpoints." },
    { title: "Edge Network", desc: "Global caching and localized delivery." },
    { title: "Deployment Layer", desc: "Immutable atomic infrastructure builds." },
    { title: "Secure DNS", desc: "Protective routing and DDoS mitigation." },
    { title: "Monitoring System", desc: "Real-time health and telemetry tracking." }
];

const TEAMS_DATA = [
    { title: "Digital Agencies", desc: "Predictable, multi-tenant infrastructure scaling for simultaneous client deployments." },
    { title: "SaaS Platforms", desc: "High-availability architecture ensuring bounded latency during dynamic usage loads." },
    { title: "Corporate Websites", desc: "Isolated environments prioritizing compliance, security, and global edge caching." },
    { title: "E-commerce Brands", desc: "Elastic compute provisioning accommodating unpredictable transactional traffic spikes." }
];

export default function Home() {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [activePlan, setActivePlan] = useState<Plan | null>(null);

    // Form State
    const [email, setEmail] = useState("");
    const [domain, setDomain] = useState("");
    const [company, setCompany] = useState("");

    const [errors, setErrors] = useState<{ email?: string; domain?: string }>({});
    const [globalError, setGlobalError] = useState("");

    const [isProcessing, setIsProcessing] = useState(false);
    const [isSuccess, setIsSuccess] = useState(false);

    // Lock scroll when modal is open
    useEffect(() => {
        if (isModalOpen) {
            document.body.style.overflow = "hidden";
        } else {
            document.body.style.overflow = "auto";
        }

        const handleEsc = (e: KeyboardEvent) => {
            if (e.key === "Escape" && isModalOpen) closeModal();
        };

        window.addEventListener("keydown", handleEsc);
        return () => window.removeEventListener("keydown", handleEsc);
    }, [isModalOpen]);

    const openModal = (plan: Plan) => {
        setActivePlan(plan);
        setIsModalOpen(true);
        setIsSuccess(false);
        resetForm();
    };

    const closeModal = () => {
        if (isProcessing) return;
        setIsModalOpen(false);
        setTimeout(() => {
            resetForm();
            setActivePlan(null);
        }, 300);
    };

    const resetForm = () => {
        setEmail("");
        setDomain("");
        setCompany("");
        setErrors({});
        setGlobalError("");
    };

    const validateForm = () => {
        const newErrors: { email?: string; domain?: string } = {};
        let isValid = true;

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!email) {
            newErrors.email = "Required";
            isValid = false;
        } else if (!emailRegex.test(email)) {
            newErrors.email = "Invalid email";
            isValid = false;
        }

        if (!domain) {
            newErrors.domain = "Required";
            isValid = false;
        } else if (domain.trim().length < 4 || !domain.includes(".")) {
            newErrors.domain = "Invalid domain";
            isValid = false;
        }

        setErrors(newErrors);
        return isValid;
    };

    const startPayment = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!validateForm() || !activePlan) return;

        setIsProcessing(true);
        setGlobalError("");

        try {
            // Create order on the server
            const res = await fetch('/api/create-order', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ amount: activePlan.total * 100 })
            });
            const data = await res.json();

            if (!res.ok) throw new Error(data.error || "Failed to create order");

            const options = {
                key: process.env.NEXT_PUBLIC_RAZORPAY_KEY_ID, // Use the public key from env
                amount: activePlan.total * 100,
                currency: "INR",
                name: "RoomitHosting",
                description: `${activePlan.name} Access`,
                order_id: data.id,
                handler: function (response: any) {
                    setIsProcessing(false);
                    setIsSuccess(true);
                },
                prefill: {
                    email: email,
                },
                theme: {
                    color: "#111111",
                },
                modal: {
                    ondismiss: function () {
                        setIsProcessing(false);
                    }
                }
            };

            // @ts-ignore
            const rzp = new window.Razorpay(options);
            rzp.on("payment.failed", function (response: any) {
                setIsProcessing(false);
                setGlobalError("Payment initialization failed. Please contact support.");
            });
            rzp.open();
        } catch (error) {
            setIsProcessing(false);
            setGlobalError("Payment gateway offline or failed to create order.");
        }
    };

    return (
        <>
            <nav className="navbar">
                <div className="container">
                    <div className="nav-logo">
                        <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
                            <path d="M12 2L2 22h20L12 2z"></path>
                        </svg>
                        RoomitHosting
                    </div>
                    <ul className="nav-links">
                        <li><a href="#infrastructure">Infrastructure</a></li>
                        <li><a href="#workflow">Workflow</a></li>
                        <li><a href="#pricing">Pricing</a></li>
                        <li><a href="#compliance">Compliance</a></li>
                    </ul>
                    <div className="nav-actions">
                        <a href="#pricing" className="btn btn-secondary">View Plans</a>
                    </div>
                </div>
            </nav>

            <main>
                {/* Hero Section */}
                <section className="hero">
                    <div className="container">
                        <h1 className="hero-title">Deploy with Confidence.</h1>
                        <p className="hero-subtitle">
                            Enterprise-grade managed hosting infrastructure for modern businesses and agencies. Accelerate your production deployments securely.
                        </p>
                        <div className="hero-actions">
                            <a href="#workflow" className="btn btn-primary">
                                Start Deployment
                            </a>
                            <a href="#pricing" className="btn btn-secondary">
                                View Plans
                            </a>
                        </div>
                    </div>
                </section>

                {/* Infrastructure */}
                <motion.section
                    id="infrastructure"
                    className="section no-border infra-section"
                    initial="hidden"
                    whileInView="visible"
                    viewport={{ once: true, margin: "-100px" }}
                    variants={{
                        hidden: { opacity: 0, y: 20 },
                        visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: "easeOut", staggerChildren: 0.1 } }
                    }}
                >
                    <div className="container">
                        <div className="infra-header">
                            <span className="infra-label">INFRASTRUCTURE</span>
                            <h2 className="infra-title">Built for Reliability at Scale.</h2>
                            <p className="infra-subtitle">Enterprise-grade architecture designed for stability, performance, and security.</p>
                        </div>

                        <div className="infra-grid">
                            {INFRASTRUCTURE_FEATURES.map((feat, idx) => (
                                <motion.div
                                    key={idx}
                                    className="infra-card"
                                    variants={{
                                        hidden: { opacity: 0, y: 20 },
                                        visible: { opacity: 1, y: 0 }
                                    }}
                                    whileHover={{ scale: 1.02, y: -4 }}
                                    transition={{ duration: 0.4, ease: "easeOut" }}
                                >
                                    <div className="infra-card-icon">
                                        <motion.div
                                            initial={{ scale: 0.8, opacity: 0 }}
                                            whileInView={{ scale: 1, opacity: 1 }}
                                            transition={{ duration: 0.3, delay: 0.1 + idx * 0.1 }}
                                            viewport={{ once: true }}
                                        >
                                            {feat.icon}
                                        </motion.div>
                                    </div>
                                    <h3 className="infra-card-title">{feat.title}</h3>
                                    <p className="infra-card-desc">{feat.desc}</p>
                                </motion.div>
                            ))}
                        </div>
                    </div>
                </motion.section>

                {/* Platform Architecture */}
                <section className="section bg-surface-alt">
                    <div className="container">
                        <div className="infra-header">
                            <h2 className="section-title" style={{ marginBottom: "0.5rem" }}>Platform Architecture</h2>
                            <p className="section-subtitle" style={{ marginBottom: "2rem" }}>A highly resilient, horizontal deployment lifecycle engineered for global reach.</p>
                        </div>
                        <div className="arch-flow">
                            {ARCHITECTURE_STEPS.map((step, idx) => (
                                <React.Fragment key={idx}>
                                    <motion.div
                                        className="arch-card"
                                        initial={{ opacity: 0, y: 15 }}
                                        whileInView={{ opacity: 1, y: 0 }}
                                        viewport={{ once: true, margin: "-50px" }}
                                        transition={{ duration: 0.5, delay: idx * 0.15 }}
                                    >
                                        <h4>{step.title}</h4>
                                        <p>{step.desc}</p>
                                    </motion.div>

                                    {idx < ARCHITECTURE_STEPS.length - 1 && (
                                        <motion.div
                                            className="arch-connector"
                                            initial={{ opacity: 0 }}
                                            whileInView={{ opacity: 1 }}
                                            viewport={{ once: true }}
                                            transition={{ duration: 0.4, delay: idx * 0.15 + 0.2 }}
                                        >
                                            <div className="arch-connector-flow" style={{ animationDelay: `${idx * 0.3}s` }}></div>
                                        </motion.div>
                                    )}
                                </React.Fragment>
                            ))}
                        </div>
                    </div>
                </section>

                {/* Built for Teams */}
                <section className="section">
                    <div className="container" style={{ maxWidth: "1000px" }}>
                        <div className="infra-header">
                            <h2 className="section-title" style={{ marginBottom: "0.5rem" }}>Built for Teams That Ship</h2>
                            <p className="section-subtitle" style={{ marginBottom: "3rem" }}>Reliable infrastructure parameters aligned to specific production requirements.</p>
                        </div>
                        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: "1.5rem" }}>
                            {TEAMS_DATA.map((team, idx) => (
                                <motion.div
                                    key={idx}
                                    style={{
                                        background: "rgba(255, 255, 255, 0.02)",
                                        border: "1px solid var(--border-color)",
                                        borderRadius: "var(--radius-xl)",
                                        padding: "2rem",
                                        display: "flex",
                                        flexDirection: "column"
                                    }}
                                    initial={{ opacity: 0, y: 15 }}
                                    whileInView={{ opacity: 1, y: 0 }}
                                    viewport={{ once: true, margin: "-50px" }}
                                    transition={{ duration: 0.4, delay: idx * 0.1 }}
                                >
                                    <h3 style={{ fontSize: "1.125rem", fontWeight: 600, color: "var(--text-primary)", marginBottom: "0.75rem" }}>
                                        {team.title}
                                    </h3>
                                    <p style={{ fontSize: "0.875rem", color: "var(--text-secondary)", lineHeight: 1.6, margin: 0 }}>
                                        {team.desc}
                                    </p>
                                </motion.div>
                            ))}
                        </div>
                    </div>
                </section>

                {/* How It Works */}
                <section id="workflow" className="section">
                    <div className="container">
                        <h2 className="section-title">Deployment Workflow</h2>
                        <p className="section-subtitle">Streamlined zero-downtime infrastructure provisioning process.</p>

                        <div className="steps-container">
                            <div className="step-card">
                                <span className="step-number">01</span>
                                <div className="step-content">
                                    <h3 className="step-title">Submit Deployment Request</h3>
                                    <p className="step-desc">Configure your domain and workload parameters through our secure portal.</p>
                                </div>
                            </div>
                            <div className="step-card">
                                <span className="step-number">02</span>
                                <div className="step-content">
                                    <h3 className="step-title">Infrastructure Setup & Configuration</h3>
                                    <p className="step-desc">Our automated systems provision compute resources, set up global edges, and configure origin connections securely.</p>
                                </div>
                            </div>
                            <div className="step-card">
                                <span className="step-number">03</span>
                                <div className="step-content">
                                    <h3 className="step-title">Secure Deployment & Monitoring</h3>
                                    <p className="step-desc">Your traffic is routed through encrypted pathways. Health checks and telemetry systems are activated.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                {/* Pricing / Access */}
                <section id="pricing" className="section">
                    <div className="container">
                        <h2 className="section-title">Plans & Infrastructure Access</h2>
                        <p className="section-subtitle">One-time infrastructure setup fee. No recurring hosting charges.</p>

                        <div className="grid pricing-grid">
                            {PLANS.map((plan) => (
                                <div key={plan.id} className={`pricing-card ${plan.popular ? 'business' : ''}`}>
                                    <h3 className="plan-name">{plan.name}</h3>
                                    <div className="plan-subtext">{plan.desc}</div>
                                    <div className="plan-price">
                                        ₹{plan.total.toLocaleString("en-IN")}
                                    </div>
                                    <div className="plan-subtext" style={{ minHeight: 'auto', marginBottom: '1.5rem' }}>
                                        ₹{plan.price.toLocaleString("en-IN")} + 18% GST
                                    </div>

                                    <ul className="plan-features">
                                        {plan.features.map((feat, idx) => (
                                            <li key={idx}>
                                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                                                {feat}
                                            </li>
                                        ))}
                                    </ul>

                                    <button
                                        className={plan.popular ? "btn btn-primary" : "btn btn-secondary"}
                                        onClick={() => openModal(plan)}
                                    >
                                        {plan.buttonText}
                                    </button>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>

                {/* Security & Compliance */}
                <section id="compliance" className="section">
                    <div className="container">
                        <h2 className="section-title">Security & Compliance</h2>
                        <p className="section-subtitle">Engineered to meet stringent regulatory requirements.</p>

                        <div className="security-grid">
                            <div className="security-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                                GST Compliant Billing
                            </div>
                            <div className="security-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                                Secure Payment Gateway
                            </div>
                            <div className="security-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"></path></svg>
                                Encrypted Traffic (HTTPS)
                            </div>
                            <div className="security-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                                Data Privacy Commitment
                            </div>
                        </div>
                    </div>
                </section>

            </main>

            <footer className="footer">
                <div className="container">
                    <div className="footer-content">
                        <div className="footer-brand">
                            <div className="footer-logo">
                                <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20" style={{ display: 'inline-block', marginRight: '8px', verticalAlign: 'middle' }}>
                                    <path d="M12 2L2 22h20L12 2z"></path>
                                </svg>
                                RoomitHosting
                            </div>
                            <div className="footer-desc">
                                Managed Infrastructure Division.
                            </div>
                        </div>
                        <div className="footer-links-container">
                            <div className="footer-links-group">
                                <h4>Platform</h4>
                                <ul className="footer-links">
                                    <li><a href="#infrastructure">Infrastructure</a></li>
                                    <li><a href="#workflow">Deployment</a></li>
                                    <li><a href="#pricing">Pricing</a></li>
                                </ul>
                            </div>
                            <div className="footer-links-group">
                                <h4>Resources</h4>
                                <ul className="footer-links">
                                    <li><a href="#">Documentation</a></li>
                                    <li><a href="#">System Status</a></li>
                                    <li><a href="#">Support</a></li>
                                </ul>
                            </div>
                            <div className="footer-links-group">
                                <h4>Legal</h4>
                                <ul className="footer-links">
                                    <li><a href="/terms">Terms of Service</a></li>
                                    <li><a href="/privacy">Privacy Policy</a></li>
                                    <li><a href="#">Contact</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div className="footer-bottom">
                        <span>© {new Date().getFullYear()} RoomitHosting. All rights reserved.</span>
                        <div style={{ display: 'flex', gap: '1rem' }}>
                            <a href="#">Status: All systems normal</a>
                        </div>
                    </div>
                </div>
            </footer>

            {/* Checkout Modal */}
            {isModalOpen && activePlan && (
                <div className="modal-overlay" onClick={(e) => {
                    if (e.target === e.currentTarget) closeModal();
                }}>
                    <div className="modal-content" role="dialog" aria-modal="true">
                        {!isProcessing && (
                            <button className="close-btn" onClick={closeModal} aria-label="Close modal">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ width: 18, height: 18 }}><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                            </button>
                        )}

                        {!isSuccess ? (
                            <>
                                <div className="modal-left">
                                    <div className="modal-title">Order Summary</div>
                                    <div className="summary-list">
                                        <div className="summary-item">
                                            <span>{activePlan.name} Access</span>
                                            <span>₹{activePlan.price.toLocaleString("en-IN")}</span>
                                        </div>
                                        <div className="summary-item">
                                            <span>GST (18%)</span>
                                            <span>₹{activePlan.gst.toLocaleString("en-IN")}</span>
                                        </div>
                                    </div>
                                    <div className="summary-total">
                                        <span>Total</span>
                                        <span>₹{activePlan.total.toLocaleString("en-IN")}</span>
                                    </div>
                                    <p style={{ marginTop: '2rem', fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
                                        Infrastructure setup is billed as a one-time fee. No recurring charges.
                                    </p>
                                </div>
                                <div className="modal-right">
                                    <div className="modal-title">Payment Details</div>
                                    <form onSubmit={startPayment} noValidate>
                                        <div className="form-group">
                                            <label htmlFor="businessEmail">Business Email</label>
                                            <input
                                                type="email"
                                                id="businessEmail"
                                                placeholder="you@company.com"
                                                value={email}
                                                onChange={(e) => { setEmail(e.target.value); setErrors(p => ({ ...p, email: '' })); }}
                                                className={errors.email ? "error" : ""}
                                                disabled={isProcessing}
                                            />
                                            {errors.email && <div className="form-error">{errors.email}</div>}
                                        </div>

                                        <div className="form-group">
                                            <label htmlFor="websiteDomain">Domain Target</label>
                                            <input
                                                type="text"
                                                id="websiteDomain"
                                                placeholder="api.example.com"
                                                value={domain}
                                                onChange={(e) => { setDomain(e.target.value); setErrors(p => ({ ...p, domain: '' })); }}
                                                className={errors.domain ? "error" : ""}
                                                disabled={isProcessing}
                                            />
                                            {errors.domain && <div className="form-error">{errors.domain}</div>}
                                        </div>

                                        <div className="form-group">
                                            <label htmlFor="companyName">Company / Organization (Optional)</label>
                                            <input
                                                type="text"
                                                id="companyName"
                                                placeholder="Acme Corp"
                                                value={company}
                                                onChange={(e) => setCompany(e.target.value)}
                                                disabled={isProcessing}
                                            />
                                        </div>

                                        {globalError && <div className="form-error" style={{ marginBottom: '1rem' }}>{globalError}</div>}

                                        <div className="modal-footer">
                                            <button
                                                type="submit"
                                                className="btn btn-primary"
                                                disabled={isProcessing}
                                            >
                                                {isProcessing ? "Processing Configuration..." : `Confirm Payment`}
                                            </button>

                                            <div className="secure-badge">
                                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                                                Secure Payment Powered by Razorpay
                                            </div>
                                        </div>
                                    </form>
                                </div>
                            </>
                        ) : (
                            <div className="modal-right" style={{ flex: 1, textAlign: 'center', padding: '4rem 2.5rem' }}>
                                <div style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', width: '48px', height: '48px', borderRadius: '50%', background: 'rgba(255,255,255,0.1)', color: 'var(--text-primary)', marginBottom: '1.5rem' }}>
                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ width: 24, height: 24 }}><polyline points="20 6 9 17 4 12"></polyline></svg>
                                </div>
                                <h2 style={{ fontSize: '1.5rem', fontWeight: 600, marginBottom: '0.5rem' }}>Configuration Initiated</h2>
                                <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem', fontSize: '0.9375rem' }}>
                                    Your infrastructure request for <strong>{domain}</strong> has been received securely.
                                </p>
                                <button type="button" className="btn btn-secondary" onClick={closeModal}>
                                    Return to Overview
                                </button>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </>
    );
}
