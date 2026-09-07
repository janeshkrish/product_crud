import { useEffect, useState } from "react";
import axios from "axios";

import ProductForm from "./components/ProductForm";
import ProductTable from "./components/ProductTable";

import "./App.css";
import logo from "./assets/logo.jpeg";


const API_URL = "http://localhost:8000";


function App() {

    const [products, setProducts] = useState([]);

    const [editingProduct, setEditingProduct] =
        useState(null);


    const fetchProducts = async () => {

        try {

            const response = await axios.get(
                `${API_URL}/products`
            );

            setProducts(response.data);

        } catch (error) {

            console.error(
                "Failed to fetch products",
                error
            );

        }

    };


    useEffect(() => {

        fetchProducts();

    }, []);


    const handleDelete = async (productId) => {

        const confirmed = window.confirm(
            "Are you sure you want to delete this product?"
        );

        if (!confirmed) {
            return;
        }


        try {

            await axios.delete(
                `${API_URL}/products/${productId}`
            );

            fetchProducts();

        } catch (error) {

            console.error(error);

            alert("Failed to delete product");

        }

    };


    const handleEdit = (product) => {

        setEditingProduct(product);

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    };


    const handleSuccess = () => {

        setEditingProduct(null);

        fetchProducts();

    };


    return (

        <div className="app">

            <header className="page-header">

    <img
        src={logo}
        alt="Yatzar Logo"
        className="logo"
    />

    <div>
        <p className="eyebrow">
            PRODUCT MANAGEMENT
        </p>

        <h1>
            Product Dashboard
        </h1>

        <p className="subtitle">
            Create, update and manage your products
        </p>
    </div>

</header>


            <main className="container">

                <ProductForm
                    editingProduct={editingProduct}
                    onSuccess={handleSuccess}
                    onCancel={() =>
                        setEditingProduct(null)
                    }
                />


                <ProductTable
                    products={products}
                    onEdit={handleEdit}
                    onDelete={handleDelete}
                />

            </main>

        </div>

    );
}

export default App;