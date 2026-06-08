-- Seed data for petra_cookies database
-- Run after schema.sql: mysql -u root -p petra_cookies < database/seed.sql

SET NAMES utf8mb4;
USE `petra_cookies`;

-- admins (password: admin123 hashed with bcrypt)
INSERT INTO `admins` (`id`, `username`, `email`, `password`, `created_at`) VALUES
(1, 'admin', 'admin@petracookies.com', '$2b$12$zAGlAHGwIeopk06.Iyr/kesmFXjRPCA8tqILuvmOOpEMpXUOTohKG', '2026-06-02 17:25:26');

-- categories
INSERT INTO `categories` (`id`, `name`, `slug`, `description`, `created_at`) VALUES
(6,  'Kue Kering',       'kue-kering',         'Aneka kue kering renyah untuk berbagai kesempatan', '2026-06-02 23:07:41'),
(7,  'Snack & Kue Basah','snack-&-kue-basah',   NULL, '2026-06-02 23:07:41'),
(8,  'Roti, Pastry & Sus','roti,-pastry-&-sus',  NULL, '2026-06-02 23:07:41'),
(10, 'Bolu & Cake',      'bolu-&-cake',          NULL, '2026-06-06 23:37:02'),
(11, 'Custom',           'custom',               NULL, '2026-06-06 23:54:51');

-- articles
INSERT INTO `articles` (`id`, `admin_id`, `title`, `slug`, `content`, `excerpt`, `image`, `is_published`, `published_at`, `created_at`, `updated_at`) VALUES
(1, 1, 'Tips Menyimpan Kue Kering dan Kue Basah Agar Tetap Lezat', 'tips-menyimpan-kue-kering-dan-kue-basah-agar-tetap-lezat',
 'Penyimpanan yang tepat sangat penting untuk menjaga kualitas kue. Kue kering sebaiknya disimpan dalam wadah kedap udara dan ditempatkan di area yang sejuk serta kering agar tetap renyah dan tidak mudah melempem.\r\n\r\nSementara itu, kue basah memiliki kadar air yang lebih tinggi sehingga lebih cepat rusak. Oleh karena itu, kue basah sebaiknya disimpan dalam wadah tertutup dan dimasukkan ke dalam lemari pendingin jika tidak langsung dikonsumsi.\r\n\r\nDengan cara penyimpanan yang sesuai, baik kue kering maupun kue basah dapat tetap terjaga rasa, tekstur, dan kualitasnya lebih lama. 🍪🍰✨',
 'Cara penyimpanan yang tepat dapat menjaga rasa dan kualitas kue lebih lama. Simak tips menyimpan kue kering dan kue basah agar tetap lezat saat dinikmati.',
 'blog2.png', 1, '2026-06-02 17:25:26', '2026-06-02 17:25:26', '2026-06-08 06:53:18'),

(2, 1, 'Perbedaan Kue Kering, Kue Basah, dan Pastry', 'perbedaan-kue-kering-kue-basah-dan-pastry',
 '🍪Kue kering memiliki tekstur renyah dan dapat disimpan dalam waktu yang cukup lama, seperti nastar, kastengel, dan putri salju.\r\n\r\n🍮Kue basah memiliki tekstur yang lembut dan kadar air yang lebih tinggi sehingga masa simpannya lebih singkat. Contohnya adalah lapis, lemper, dan bolu kukus.\r\n\r\n🥐Sementara itu, pastry adalah produk olahan adonan berlapis yang menggunakan banyak mentega sehingga menghasilkan tekstur yang renyah dan berlapis-lapis. Contoh pastry yang populer adalah croissant, puff pastry, dan danish pastry.\r\nDengan memahami perbedaannya, Anda dapat memilih jenis camilan yang sesuai dengan selera dan kebutuhan Anda.',
 'Kue kering, kue basah, dan pastry memiliki karakteristik yang berbeda dari segi tekstur, bahan, serta daya tahan. Kenali perbedaannya agar lebih mudah memilih camilan favorit.',
 'blog1.png', 1, '2026-06-02 17:25:26', '2026-06-02 17:25:26', '2026-06-08 06:53:10'),

(3, 1, 'Apa Perbedaan Bolu, Brownies, dan Chiffon ?', 'apa-perbedaan-bolu-brownies-dan-chiffon-',
 'Bolu memiliki tekstur yang lembut dan empuk sehingga cocok dinikmati oleh semua kalangan. Kue ini sering menjadi pilihan untuk berbagai acara karena rasanya yang ringan.\r\n\r\nBrownies memiliki tekstur yang lebih padat dan lembap dibandingkan bolu. Kandungan cokelat dan mentega yang lebih banyak membuat rasanya lebih kaya dan cocok bagi pencinta cokelat.\r\n\r\nSementara itu, chiffon cake terkenal karena teksturnya yang sangat ringan dan lembut. Kue ini dibuat menggunakan teknik khusus yang membuatnya mengembang tinggi dan terasa halus saat disantap.',
 'Sama-sama lezat, tetapi bolu, brownies, dan chiffon cake memiliki keunikan tersendiri. Cari tahu perbedaannya di sini! 🍰✨',
 'blog3.png', 1, '2026-06-07 20:03:23', '2026-06-07 20:03:23', '2026-06-08 06:54:04');

-- faqs
INSERT INTO `faqs` (`id`, `question`, `answer`, `sort_order`, `is_active`, `created_at`) VALUES
(1, 'Bagaimana cara memesan produk Petra Cookies?', 'Kamu bisa memesan langsung melalui WhatsApp kami. Kami siap membantu proses pemesanan kamu dengan mudah dan cepat.', 1, 1, '2026-06-03 08:18:48'),
(2, 'Berapa minimum pemesanan?', 'Minimum pemesanan adalah 25 pcs untuk produk tertentu. Untuk informasi lebih lanjut mengenai produk yang tersedia, silakan hubungi kami.', 2, 1, '2026-06-03 08:18:48'),
(3, 'Apakah tersedia pengiriman?', 'Ya, kami melayani pengiriman namun hanya untuk jarak tertentu. Untuk informasi lebih lanjut mengenai jangkauan pengiriman, silakan tanyakan langsung kepada kami.', 3, 1, '2026-06-03 08:18:48'),
(4, 'Berapa lama waktu pembuatan pesanan?', 'Waktu pembuatan tergantung dari jumlah pesanan dan kesepakatan awal. Kami sarankan untuk menghubungi kami lebih awal agar pesanan bisa dipersiapkan dengan baik.', 4, 1, '2026-06-03 08:18:48'),
(5, 'Apakah produk menggunakan bahan pengawet?', 'Tidak. Semua produk kami dibuat dari bahan-bahan pilihan tanpa bahan pengawet, sehingga aman untuk dikonsumsi oleh seluruh keluarga.', 5, 1, '2026-06-03 08:18:48');

-- gallery
INSERT INTO `gallery` (`id`, `type`, `title`, `description`, `image`, `author_name`, `rating`, `is_active`, `created_at`) VALUES
(1,  'testimonial', NULL, 'Food: 5\r\nService: 5\r\nAtmosphere: 5', NULL, 'Andreas Rio', 5, 1, '2026-06-02 17:25:26'),
(2,  'testimonial', NULL, 'mantulll sangat Nikmat', NULL, 'Sunarti', 5, 1, '2026-06-02 17:25:26'),
(3,  'testimonial', NULL, NULL, NULL, 'Destri Stefani', 5, 1, '2026-06-02 17:25:26'),
(8,  'testimonial', NULL, 'maknyus', NULL, 'Didik Nugroho SPd', 5, 1, '2026-06-06 06:56:01'),
(9,  'testimonial', NULL, 'enak banget bikin ketagihannn', NULL, 'susi 2', 5, 1, '2026-06-06 19:59:59'),
(10, 'testimonial', NULL, 'kue-kue nya berkwalitas dan bs custom sesuai keinginan sendiri.', NULL, 'isaa syaa', 5, 1, '2026-06-06 20:00:23'),
(11, 'testimonial', NULL, 'rasanya enak, pelayanannya ramah dan memuaskan, recommended buat yang cari kue rumahan', NULL, 'Adellia Woojin', 5, 1, '2026-06-06 20:00:49'),
(12, 'testimonial', NULL, 'Rasanya sangat enak, manisnya pas jadi langganan terus deh', NULL, 'vatim', 5, 1, '2026-06-06 20:01:29'),
(13, 'testimonial', NULL, 'enakkk bgttt pasti langganan lagi', NULL, 'Cahya', 5, 1, '2026-06-06 20:01:54'),
(16, 'testimonial', NULL, 'kuenya enakk bgtt top pokok e', NULL, 'Utari', 5, 1, '2026-06-06 22:12:44'),
(17, 'testimonial', NULL, 'Masya Allah, kuenya enak sekali rasanya emang mantul, enak banget. Pelayanannya juga ramah dan memuaskan. Sukses selalu ya, bakalan jadi langganan ini mah.', NULL, 'sari lestari', 5, 1, '2026-06-06 22:13:36'),
(18, 'testimonial', NULL, 'Kue dibuat sesuai request, memuaskan sangat menarik👍🏻', NULL, 'juwita', 5, 1, '2026-06-06 22:14:35'),
(19, 'testimonial', NULL, 'jossshhhh top markotop👍🏻👍🏻👍🏻\r\nakan pesan lagi klo ada acara...', NULL, 'Ida.septiana', 5, 1, '2026-06-06 22:15:21'),
(20, 'photo', 'Mengikuti PNFest 2024', 'Meraih penghargaan dalam ajang PNFest 2024 Surakarta atas kualitas, cita rasa, kreativitas, dan inovasi produk kue yang dihasilkan.', 'galeri.png', NULL, NULL, 1, '2026-06-08 13:43:41');

-- products
INSERT INTO `products` (`id`, `category_id`, `name`, `slug`, `description`, `price`, `price_type`, `image`, `is_active`, `created_at`, `updated_at`) VALUES
(65, 10, 'Brownise Hias',            'brownise-hias',            'Brownies cokelat dengan tekstur lembut dan padat, dipadukan dengan cita rasa cokelat yang kaya serta topping hias cokelat yang manis.', 3000.00, 'pcs',  '53.png', 1, '2026-06-08 13:24:17', '2026-06-08 13:24:17'),
(66, 11, 'Tumpeng Snack Tradisional', 'tumpeng-snack-tradisional', 'Tumpeng Snack Tradisional berisi aneka jajanan dan kue pilihan yang disusun dalam bentuk tumpeng, dengan isi yang dapat disesuaikan sesuai permintaan pelanggan.', 0.00, NULL, '21.png', 1, '2026-06-08 13:25:24', '2026-06-08 13:25:24'),
(67, 6,  'Sagu Keju',                'sagu-keju',                'Sagu keju memiliki tekstur yang garing, ringan, dan mudah hancur saat digigit. Rasanya cenderung gurih karena dominasi keju, dengan sedikit sentuhan manis yang seimbang.', 55000.00, 'pack', '26.png', 1, '2026-06-08 13:25:58', '2026-06-08 13:26:05'),
(68, 8,  'Pie Buah',                 'pie-buah',                 'Kulit pie yang renyah dipadukan dengan vla lembut dan creamy dengan topping buah segar yang memberikan perpaduan rasa manis dan seimbang dalam setiap gigitan.', 3000.00, 'pcs',  '8.png',  1, '2026-06-08 13:26:59', '2026-06-08 13:26:59'),
(69, 7,  'Pastel Sayur',             'pastel-sayur',             'Perpaduan kulit pastel yang renyah dengan isian sayur yang gurih dan lembut, menghasilkan rasa yang ringan namun memuaskan.', 2500.00, 'pcs',  '30.png', 1, '2026-06-08 13:27:41', '2026-06-08 14:39:37');
