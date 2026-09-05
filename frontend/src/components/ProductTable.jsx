const API_URL = "http://localhost:8000";

function ProductTable({
    products,
    onEdit,
    onDelete
}) {

    return (

        <div className="table-card">

            <div className="table-header">

                <div>

                    <h2>
                        Products
                    </h2>

                    <p>
                        {products.length} products found
                    </p>

                </div>

            </div>


            <div className="table-container">

                <table>

                    <thead>

                        <tr>

                            <th>Image</th>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Price</th>
                            <th>Status</th>
                            <th>Actions</th>

                        </tr>

                    </thead>


                    <tbody>

                        {products.length === 0 ? (

                            <tr>

                                <td
                                    colSpan="6"
                                    className="empty"
                                >
                                    No products found
                                </td>

                            </tr>

                        ) : (

                            products.map((product) => (

                                <tr key={product.product_id}>

                                    <td>

                                        {product.product_image ? (

                                            <img
                                                className="product-thumb"
                                                src={`${API_URL}/${product.product_image}`}
                                                alt={product.product_name}
                                            />

                                        ) : (

                                            <div className="no-image">
                                                No Image
                                            </div>

                                        )}

                                    </td>


                                    <td>
                                        {product.product_id}
                                    </td>


                                    <td>
                                        {product.product_name}
                                    </td>


                                    <td>
                                        ₹{product.product_price}
                                    </td>


                                    <td>

                                        <span
                                            className={
                                                product.product_status === "Active"
                                                    ? "status active"
                                                    : "status inactive"
                                            }
                                        >
                                            {product.product_status}
                                        </span>

                                    </td>


                                    <td>

                                        <div className="actions">

                                            <button
                                                className="edit-btn"
                                                onClick={() =>
                                                    onEdit(product)
                                                }
                                            >
                                                Edit
                                            </button>

                                            <button
                                                className="delete-btn"
                                                onClick={() =>
                                                    onDelete(
                                                        product.product_id
                                                    )
                                                }
                                            >
                                                Delete
                                            </button>

                                        </div>

                                    </td>

                                </tr>

                            ))

                        )}

                    </tbody>

                </table>

            </div>

        </div>

    );
}

export default ProductTable;