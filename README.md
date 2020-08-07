# KieuTheVinh_19020486_Nhom3_Crawler

Mô tả source code: 
-start_urls : home page của trang web
-Hàm parse: + Lấy thông tin cần thu thập
	    + Lặp lại quá trình ( callback hàm parse )
-Các việc đã thực hiện: + crawl một trang đích và lấy ra thông tin cần thu thập từ một trang đó
                         + viết code lặp lại quá trình thu thập và sửa lại start_urls thành home page của web
-Kết quả: 
	+dantri.com.vn : link,tiêu đề,mô tả, tác giả, tags, thời gian đăng. Số lượng thu được trong 1h: 20525
	+fptplay.vn : link, tên phim, tóm tắt, đạo diễn, diễn viên. Số lượng thu được trong 1h: 3751
	+thegioididong.com : link, tag, giá sản phẩm, image-src, thông số. Số lượng thu được sau 1h: 
Note: thegioididong.com đã chặn ip do crawl quá nhiều, khi bật vpn thì crawl được bình thường, vì một lý do nào đó mà 
get status 200 về rất nhiều nhưng số lượng sản phẩm ghi lên file lại rất ít, em sẽ cố gắng sửa lỗi và thử làm trên trang thương mại điện tử khác