"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import useAuthStore from "@/store/authstore";
import UploadSection from "@/components/ui/dashboard/UploadSection";

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

    const handleLogout = () => {
        logout();
        router.push("/");
    }

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
<div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">

    <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-lg">
            Documents
        </h2>

        <p className="text-3xl mt-4 font-bold">
            0
        </p>
    </div>

    <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-lg">
            AI Summaries
        </h2>

        <p className="text-3xl mt-4 font-bold">
            0
        </p>
    </div>

    <div className="bg-white rounded-xl shadow p-6">
        <h2 className="font-semibold text-lg">
            Storage
        </h2>

        <p className="text-3xl mt-4 font-bold">
            0 MB
        </p>
    </div>

</div>
<div className="mt-10 bg-white rounded-xl shadow p-8">

        <UploadSection />

    <p className="text-gray-500">
        Drag & drop your PDF, DOCX or TXT file here.
    </p>

</div>
            </div>
        </main>
    );
}