"use client"

import { redirect } from "next/navigation";
import useAuthStore from "@/store/authstore";

export default function Home() {
    const { isAuthenticated } = useAuthStore();
    console.log("isAuthenticated:", isAuthenticated);

    if (isAuthenticated) {
        redirect("/dashboard");
    } else {
        redirect("/login");
    }
}