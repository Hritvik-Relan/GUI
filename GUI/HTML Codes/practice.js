document.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".garden").addEventListener("click", plantFlower);
});

function plantFlower(event) {
    const flower = document.createElement("img");
    flower.className = "flower";
    flower.src = getRandomFlower();
    flower.style.left = `${event.clientX - 25}px`;
    flower.style.top = `${event.clientY - 25}px`;

    document.querySelector(".garden").appendChild(flower);
}

function getRandomFlower() {
    const flowers = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Simple_red_flower.svg/512px-Simple_red_flower.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Simple_yellow_flower.svg/512px-Simple_yellow_flower.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Simple_purple_flower.svg/512px-Simple_purple_flower.svg.png"
    ];
    return flowers[Math.floor(Math.random() * flowers.length)];
}
