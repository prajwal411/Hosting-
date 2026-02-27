import { NextResponse } from 'next/server';
import Razorpay from 'razorpay';

export async function POST(req: Request) {
    try {
        const { amount } = await req.json();

        // Initialize Razorpay
        const instance = new Razorpay({
            key_id: process.env.NEXT_PUBLIC_RAZORPAY_KEY_ID!,
            key_secret: process.env.RAZORPAY_SECRET_KEY!,
        });

        // Create an order
        const options = {
            amount: amount, // amount in smallest currency unit
            currency: "INR",
            receipt: `receipt_${Date.now()}`
        };

        const order = await instance.orders.create(options);

        if (!order) {
            return NextResponse.json({ error: "Some error occurred while creating order" }, { status: 500 });
        }

        return NextResponse.json(order, { status: 200 });
    } catch (error) {
        console.error("Razorpay Error:", error);
        return NextResponse.json({ error: "Failed to create order" }, { status: 500 });
    }
}
