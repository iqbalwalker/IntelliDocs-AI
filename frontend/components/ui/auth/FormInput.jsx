import { Input } from "@/components/ui/input";

export default function FormInput({
    label,
    type = "text",
    ...props
}) {
    return (
        <div className="space-y-2">
            <label className="text-sm font-medium">
                {label}
            </label>

            <Input
                type={type}
                {...props}
            />
        </div>
    );
}