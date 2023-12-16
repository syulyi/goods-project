// compare_products.js

document.addEventListener('DOMContentLoaded', function() {
    // 페이지 로딩이 완료된 후에 실행될 코드
    document.getElementById('selected-image-container-1').style.display = 'block';
    document.getElementById('selected-image-container-2').style.display = 'block';
    document.getElementById('selected-image-container-3').style.display = 'block';
});

// 나머지 updateImage 함수 등은 여기에 계속 정의할 수 있음
function updateImage(productNumber) {
    var selectElement = document.getElementById('product-select-' + productNumber);
    var selectedValue = selectElement.value;
    var imageElement
//    var imageElement = document.getElementById('selected-image-');

    if (productNumber === 1) {
        imageElement = document.getElementById('selected-image-1');
//        document.getElementById('selected-image-container-1').style.display = 'block';
//        document.getElementById('selected-image-container-2').style.display = 'block';
//        document.getElementById('selected-image-container-3').style.display = 'block';
    } else if (productNumber === 2) {
        imageElement = document.getElementById('selected-image-2');
//        document.getElementById('selected-image-container-1').style.display = 'block';
//        document.getElementById('selected-image-container-2').style.display = 'block';
//        document.getElementById('selected-image-container-3').style.display = 'block';
    } else if (productNumber === 3) {
        imageElement = document.getElementById('selected-image-3');
//        document.getElementById('selected-image-container-1').style.display = 'block';
//        document.getElementById('selected-image-container-2').style.display = 'block';
//        document.getElementById('selected-image-container-3').style.display = 'block';
    }

    document.getElementById('selected-image-container-1').style.display = 'block';
    document.getElementById('selected-image-container-2').style.display = 'block';
    document.getElementById('selected-image-container-3').style.display = 'block';

    if (selectedValue === 'prod_001') {
        imageElement.src = "/static/image/kbo_samsung_001.png";
        updateProductDescription('2024 프로페셔널 선데이 모자', '42,000원', '삼성라이온즈의 24시즌 프로페셔널 선데이 모자입니다. 일요일 경기가 있을 때마다 착용합니다. 자세한 내용은 하단의 상세 설명을 꼭 확인해 주세요!');
    } else if (selectedValue === 'prod_002') {
        imageElement.src = "/static/image/kbo_samsung_002.png";
        updateProductDescription('2024 프로페셔널 선데이 모자', '42,000원', '삼성라이온즈의 24시즌 프로페셔널 선데이 모자입니다. 일요일 경기가 있을 때마다 착용합니다. 자세한 내용은 하단의 상세 설명을 꼭 확인해 주세요!');
    } else if (selectedValue === 'prod_003') {
        imageElement.src = "/static/image/kbo_samsung_003.png";
        updateProductDescription('2024 프로페셔널 선데이 모자', '42,000원', '삼성라이온즈의 24시즌 프로페셔널 선데이 모자입니다. 일요일 경기가 있을 때마다 착용합니다. 자세한 내용은 하단의 상세 설명을 꼭 확인해 주세요!');
    } else {
        imageElement.src = '/static/placeholder_image.png'
        updateProductDescription('기본 제품', '0원', '설명이 없습니다.');
    }
}

function updateProductDescription(title, price, comment) {
    document.getElementById('prod-title').innerText = title;
    document.getElementById('prod-prices').innerHTML = '<span class="prod-price">가격</span><span class="prod-price-num">' + price + '</span>';
    document.getElementById('prod-comment').innerHTML = comment;
}