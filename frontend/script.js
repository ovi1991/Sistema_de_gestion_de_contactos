const API_URL = "http://127.0.0.1:5000/api/contactos";

async function cargarContactos() {
  try {
    const res = await fetch(API_URL);
    const data = await res.json();
    const lista = document.getElementById("listaContactos");
    lista.innerHTML = "";
    data.forEach((c) => {
      const li = document.createElement("li");
      li.textContent = `${c.nombre} - ${c.telefono} - ${c.email}`;
      const btnEliminar = document.createElement("button");
      btnEliminar.textContent = "❌";
      btnEliminar.onclick = () => eliminarContacto(c.nombre);
      li.appendChild(btnEliminar);
      lista.appendChild(li);
    });
  } catch (error) {
    alert("❌ Error de conexión");
  }
}

async function agregarContacto() {
  const nombre = document.getElementById("nombre").value;
  const telefono = document.getElementById("telefono").value;
  const email = document.getElementById("email").value;

  if (!nombre || !telefono || !email) {
    alert("❌ Todos los campos son obligatorios");
    return;
  }

  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, telefono, email }),
  });

  const data = await res.json();
  if (res.ok) {
    alert("✅ Contacto agregado");
    cargarContactos();
  } else {
    alert("❌ Error: " + data.error);
  }
}

async function buscarContacto() {
  const nombre = document.getElementById("buscarNombre").value;
  const res = await fetch(`${API_URL}/${nombre}`);
  const resultado = document.getElementById("resultadoBusqueda");

  if (res.ok) {
    const contacto = await res.json();
    resultado.textContent = `${contacto.nombre} - ${contacto.telefono} - ${contacto.email } `;
  } else {
    resultado.textContent = "❌ Contacto no encontrado";
  }
}

async function eliminarContacto(nombre) {
  const res = await fetch(`${API_URL}/${nombre}`, {
    method: "DELETE",
  });
  if (res.ok) {
    alert("🗑️ Contacto eliminado");
    cargarContactos();
  } else {
    alert("❌ No se pudo eliminar");
  }
}

// Carga inicial
cargarContactos();
