// document.addEventListener("DOMContentLoaded", function() {
//     // Ẩn tất cả các nội dung của trang khi tải trang
//     const contentElements = document.querySelectorAll('.md-typeset');
//     contentElements.forEach(element => {
//         element.style.display = 'none';
//     });

//     // Hiện nội dung khi tìm kiếm
//     const searchInput = document.querySelector('input[type="search"]');
//     if (searchInput) {
//         searchInput.addEventListener('input', function() {
//             const searchTerm = this.value.toLowerCase();
//             contentElements.forEach(element => {
//                 const text = element.textContent.toLowerCase();
//                 if (text.includes(searchTerm)) {
//                     element.style.display = 'block'; // Hiện nội dung khi tìm thấy
//                 } else {
//                     element.style.display = 'none'; // Ẩn nếu không tìm thấy
//                 }
//             });
//         });
//     }
// });
