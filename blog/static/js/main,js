document.addEventListener("DOMContentLoaded", function() {
    // Simuleer bloggegevens (kan worden vervangen door een serveraanroep)
    const blogData = [
        { title: "Blog Post 1", content: "Lorem ipsum dolor sit amet..." },
        { title: "Blog Post 2", content: "Sed do eiusmod tempor incididunt..." },
        // Voeg meer bloggegevens toe zoals nodig
    ];

    const blogPostsContainer = document.getElementById("blog-posts");

    // Voeg blogposts toe aan de HTML
    blogData.forEach(post => {
        const postElement = document.createElement("article"); 
        postElement.innerHTML = `
            <h2>${post.title}</h2>
            <p>${post.content}</p>
        `;
        blogPostsContainer.appendChild(postElement);
    });
});