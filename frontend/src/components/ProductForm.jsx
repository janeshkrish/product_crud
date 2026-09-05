import { useEffect, useState } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000";

function ProductForm({
    editingProduct,
    onSuccess,
    onCancel
}) {

    const [form, setForm] = useState({
        product_id: "",
        product_name: "",
        product_price: "",
        product_status: "Active",
        product_image: null
    });

    const [preview, setPreview] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {

        if (editingProduct) {

            setForm({
                product_id: editingProduct.product_id,
                product_name: editingProduct.product_name,
                product_price: editingProduct.product_price,
                product_status: editingProduct.product_status,
                product_image: null
            });

            if (editingProduct.product_image) {

                setPreview(
                    `${API_URL}/${editingProduct.product_image}`
                );
            }

        } else {

            resetForm();

        }

    }, [editingProduct]);


    const handleChange = (e) => {

        const { name, value, files } = e.target;

        if (name === "product_image") {

            const file = files[0];

            setForm({
                ...form,
                product_image: file
            });

            if (file) {

                setPreview(
                    URL.createObjectURL(file)
                );
            }

        } else {

            setForm({
                ...form,
                [name]: value
            });

        }
    };


    const resetForm = () => {

        setForm({
            product_id: "",
            product_name: "",
            product_price: "",
            product_status: "Active",
            product_image: null
        });

        setPreview(null);
    };


    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            setLoading(true);

            const formData = new FormData();

            formData.append(
                "product_name",
                form.product_name
            );

            formData.append(
                "product_price",
                form.product_price
            );

            formData.append(
                "product_status",
                form.product_status
            );


            if (form.product_image) {

                formData.append(
                    "product_image",
                    form.product_image
                );

            }


            if (editingProduct) {

                await axios.put(
                    `${API_URL}/products/${editingProduct.product_id}`,
                    formData
                );

            } else {

                formData.append(
                    "product_id",
                    form.product_id
                );

                await axios.post(
                    `${API_URL}/products`,
                    formData
                );

            }


            resetForm();

            onSuccess();

        } catch (error) {

            console.error(error);

            alert(
                error.response?.data?.detail ||
                "Something went wrong"
            );

        } finally {

            setLoading(false);

        }

    };


    return (

        <div className="form-card">

            <div className="form-header">

                <div>

                    <h2>
                        {editingProduct
                            ? "Edit Product"
                            : "Add Product"
                        }
                    </h2>

                    <p>
                        Manage your product information
                    </p>

                </div>

            </div>


            <form onSubmit={handleSubmit}>

                <div className="form-grid">

                    {/* Product ID */}

                    <div className="form-group">

                        <label>
                            Product ID
                        </label>

                        <input
                            type="text"
                            name="product_id"
                            placeholder="e.g. PROD-001"
                            value={form.product_id}
                            onChange={handleChange}
                            disabled={!!editingProduct}
                            required
                        />

                    </div>


                    {/* Product Name */}

                    <div className="form-group">

                        <label>
                            Product Name
                        </label>

                        <input
                            type="text"
                            name="product_name"
                            placeholder="Enter product name"
                            value={form.product_name}
                            onChange={handleChange}
                            required
                        />

                    </div>


                    {/* Product Price */}

                    <div className="form-group">

                        <label>
                            Product Price
                        </label>

                        <input
                            type="number"
                            name="product_price"
                            placeholder="Enter price"
                            min="0"
                            step="0.01"
                            value={form.product_price}
                            onChange={handleChange}
                            required
                        />

                    </div>


                    {/* Product Status */}

                    <div className="form-group">

                        <label>
                            Product Status
                        </label>

                        <select
                            name="product_status"
                            value={form.product_status}
                            onChange={handleChange}
                        >

                            <option value="Active">
                                Active
                            </option>

                            <option value="Inactive">
                                Inactive
                            </option>

                        </select>

                    </div>


                    {/* Image */}

                    <div className="form-group full-width">

                        <label>
                            Product Image
                        </label>

                        <input
                            type="file"
                            name="product_image"
                            accept="image/*"
                            onChange={handleChange}
                        />

                        {preview && (

                            <div className="image-preview">

                                <img
                                    src={preview}
                                    alt="Product preview"
                                />

                            </div>

                        )}

                    </div>

                </div>


                <div className="form-actions">

                    {editingProduct && (

                        <button
                            type="button"
                            className="cancel-btn"
                            onClick={onCancel}
                        >
                            Cancel
                        </button>

                    )}

                    <button
                        type="submit"
                        className="submit-btn"
                        disabled={loading}
                    >

                        {loading
                            ? "Saving..."
                            : editingProduct
                                ? "Update Product"
                                : "Add Product"
                        }

                    </button>

                </div>

            </form>

        </div>

    );
}

export default ProductForm;