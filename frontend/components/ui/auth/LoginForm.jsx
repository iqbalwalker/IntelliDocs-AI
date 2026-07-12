"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { Button } from "@/components/ui/button";

import FormInput from "./FormInput";

import { login } from "@/services/auth.service";
import useAuthStore from "@/store/authstore";

export default function LoginForm() {
    const router = useRouter();

    const { login: loginStore, setUser } = useAuthStore();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleSubmit(e) {
        e.preventDefault();

        try {
            setLoading(true);

            const tokens = await login({
                email,
                password,
            });

            loginStore(tokens);

            const user = await getProfile();

            setUser(user);

            router.push("/dashboard");

        } catch (error) {

            console.error(error);

            alert("Invalid credentials");

        } finally {

            setLoading(false);

        }
    }

    return (
        <form
            onSubmit={handleSubmit}
            className="space-y-5"
        >
            <FormInput
                label="Email"

                value={email}

                onChange={(e) =>
                    setEmail(e.target.value)
                }
            />

            <FormInput
                label="Password"

                type="password"

                value={password}

                onChange={(e) =>
                    setPassword(e.target.value)
                }
            />

            <Button
                className="w-full"
                disabled={loading}
            >
                {loading
                    ? "Signing in..."
                    : "Sign In"}
            </Button>
        </form>
    );
}