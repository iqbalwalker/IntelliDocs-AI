"use client";

import { useState } from "react";
import { uploadDocument } from "@/services/document.service";

export default function UploadSection() {
    const [loading, setLoading] = useState(false);

    async function handleFile(e) {
        const file = e.target.files[0];

        if (!file) return;

        try {
            setLoading(true);

            const document = await uploadDocument(file);

            console.log(document);

            alert("Upload successful!");

        } catch (error) {
    console.error("UPLOAD ERROR:", error);

    if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Response:", error.response.data);
    }

    alert(JSON.stringify(error.response?.data ?? error.message));
} finally {
    setLoading(false);
}
    }

    return (
        <div className="bg-white rounded-xl shadow p-8 mt-10">

            <h2 className="text-2xl font-bold mb-6">
                Upload Document
            </h2>

            <input
                type="file"
                accept=".pdf,.docx,.txt"
                onChange={handleFile}
            />

            {loading && (
                <p className="mt-4">
                    Uploading...
                </p>
            )}

        </div>
    );
}