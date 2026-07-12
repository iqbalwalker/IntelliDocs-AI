"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import useAuthStore from "@/store/authstore";

export default function Dashboard() {
    const router = useRouter();

    const {
        isAuthenticated,
        user,
        logout,
    } = useAuthStore();

    useEffect(() => {
        if (!isAuthenticated) {
            router.replace("/");
        }
    }, [isAuthenticated, router]);

    if (!isAuthenticated) return null;

    return (
        // Dashboard UI
        <main className="min-h-screen bg-slate-100">
            <div className="max-w-6xl mx-auto p-8">

                <div className="flex justify-between items-center">

                    <div>
                        <h1 className="text-4xl font-bold">
                            IntelliDocs AI
                        </h1>

                        <p className="text-gray-500 mt-2">
                            Welcome back,
                            {" "}
                            {user?.first_name}
                        </p>
                    </div>

                    <button
                        onClick={logout}
                        className="bg-red-500 text-white px-4 py-2 rounded-lg"
                    >
                        Logout
                    </button>

                </div>

            </div>
        </main>
    );
}