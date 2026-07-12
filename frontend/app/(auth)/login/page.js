import AuthCard from "@/components/ui/auth/AuthCard";

import LoginForm from "@/components/ui/auth/LoginForm";

export default function LoginPage() {
    return (
        <AuthCard title="Welcome Back">
            <LoginForm />
        </AuthCard>
    );
}