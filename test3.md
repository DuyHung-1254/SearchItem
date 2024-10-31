<!-- Tìm kiếm Tác giả, Tác phẩm và Thể loại -->

![Image](./asset/frise_luce.png)


<div style="display: flex; align-items: center;">
    <input type="text" id="search-input" placeholder="Nhập tên tác giả, tác phẩm hoặc thể loại" style="flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px; margin-right: 10px;">
    <select id="search-type" style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; background-color: #f9f9f9;">
        <option value="author">Tác giả</option>
        <option value="work">Tác phẩm</option>
        <option value="genre">Thể loại</option>
    </select>
</div>
<div id="search-results" style="margin-top: 20px;"></div>

<!-- Thêm phần chi tiết tài liệu -->
<!-- <div id="detail-section" style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9; display: none;">
    <h2>Chi tiết tài liệu</h2>
</div> -->

<style>
    /* CSS để tạo khoảng cách giữa các kết quả tìm kiếm */
    #search-results div {
        margin-bottom: 20px; /* Khoảng cách giữa các kết quả */
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        background-color: #f9f9f9;
        cursor: pointer;
    }
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/lunr.js/2.3.9/lunr.min.js"></script>

<script>
    let idx;
    let documents;

    // Tải dữ liệu JSON
    fetch('Base_Luce.json')
        .then(response => response.json())
        .then(data => {
            documents = data;
            // Tạo chỉ mục tìm kiếm với Lunr
            createIndex();
        });

    function createIndex() {
        const selectedType = document.getElementById('search-type').value;

        idx = lunr(function () {
            this.ref('id');

            // Thêm trường vào chỉ mục dựa trên loại tìm kiếm
            if (selectedType === 'author') {
                this.field('prénom auteur');
                this.field('auteurMIN');
            } else if (selectedType === 'work') {
                this.field('titre');
            }
            // Thêm genre vào tất cả các loại tìm kiếm
            this.field('genre');

            // Thêm từng tài liệu vào index với ID duy nhất
            documents.forEach((doc, idx) => {
                this.add({ ...doc, id: idx });
            });
        });
    }

    // Cập nhật chỉ mục khi loại tìm kiếm thay đổi
    document.getElementById('search-type').addEventListener('change', createIndex);

    // Hàm xử lý tìm kiếm
    document.getElementById('search-input').addEventListener('input', function() {
        const query = this.value;
        let results = idx.search(query);

        const resultsDiv = document.getElementById('search-results');
        resultsDiv.innerHTML = '';

        if (results.length > 0) {
            results.forEach(result => {
                const doc = documents[result.ref];
                const resultItem = document.createElement('div');

                // Sử dụng sự kiện onclick để hiển thị chi tiết tài liệu
        resultItem.addEventListener('click', () => {
            window.location.href = `detailPage.html?id=${result.ref}`;
        });

                resultItem.innerHTML = `
                    <strong>Tác giả:</strong> ${doc["prénom auteur"]} ${doc["auteurMIN"]} <br>
                    <strong>Tác phẩm:</strong> ${doc["titre"]} <br>
                    <strong>Năm:</strong> ${doc["date"]} <br>
                    <strong>Thể loại:</strong> ${doc["genre"]}

                `;
                resultsDiv.appendChild(resultItem);
            });
        } else {
            resultsDiv.innerHTML = '<p>Không tìm thấy kết quả.</p>';
        }
    });

</script>
