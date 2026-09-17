import { useState } from "react";

export default function FileUpload({ onUpload, loading, hasDocument }){
    const [fileName, setFileName] = useState("");
    return (
        <div>
            <button>Upload</button>
        </div>
    );
}