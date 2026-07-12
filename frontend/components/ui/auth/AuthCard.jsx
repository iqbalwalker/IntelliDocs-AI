import { Card, CardContent } from "@/components/ui/card";

export default function AuthCard({ title, children }) {
    return (
        <div className="min-h-screen flex items-center justify-center bg-slate-50 p-4">
            <Card className="w-full max-w-md shadow-lg">
                <CardContent className="p-8">
                    <h1 className="text-3xl font-bold mb-6 text-center">
                        {title}
                    </h1>

                    {children}
                </CardContent>
            </Card>
        </div>
    );
}