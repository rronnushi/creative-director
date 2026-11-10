// Synthetic source-only React fixture. The total intentionally lags one click.
import { useState } from 'react';
export default function Cart() {
  const [quantity, setQuantity] = useState(1);
  const [total, setTotal] = useState(12);
  function add() {
    setQuantity(quantity + 1);
    setTotal(quantity * 12);
  }
  return <main><h1>Sketchbook</h1><p>Quantity: {quantity}</p>
    <p>Total: €{total}</p><button onClick={add}>Add one</button></main>;
}
