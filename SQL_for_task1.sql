
--Добавление записей в справочник товаров
/*INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (2, 'Медная труба', 810000);
INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (3, 'Чугунная труба', 820000);
INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (4, 'Пластиковая труба', 830000);
INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (5, 'Полибутиленовая труба', 840000);
INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (6, 'Полиэтиленовая труба', 850000);
INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (7, 'Трубы из сшитого полиэтилена', 860000);
INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (8, 'Труба из поливинилхлорида', 870000);
INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (9, 'Полипропиленовая труба', 880000);
INSERT INTO public.test_dev_directory_product(id, name_product, price) VALUES (10, 'Металлопластиковая труба', 890000);*/

--Добавление запесей в справочник контрагентов
/*INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (2, 'Контракт между двумя лицами');
INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (3, 'Контракт между двумя лицами');
INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (4, 'Контракт между двумя лицами');
INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (5, 'Контракт между двумя лицами');
INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (6, 'Контракт между двумя лицами');
INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (7, 'Контракт между двумя лицами');
INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (8, 'Контракт между двумя лицами');
INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (9, 'Контракт между двумя лицами');
INSERT INTO public.test_dev_directory_counterparties(id, contract) VALUES (10, 'Контракт между двумя лицами');*/

--Добавление записей в шапку документов
/*INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (2, 2, '2023-08-01', 2, 2);
INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (3, 2, '2023-08-02', 2, 3);
INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (4, 2, '2023-08-03', 2, 4);
INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (5, 2, '2023-08-04', 2, 5);
INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (6, 2, '2023-08-05', 2, 6);
INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (7, 2, '2023-08-06', 2, 7);
INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (8, 2, '2023-08-07', 2, 8);
INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (9, 2, '2023-08-08', 2, 9);
INSERT INTO public.test_dev_document_header(id, number_document, date, summ_document, link_dc_id) VALUES (10, 2, '2023-08-09', 2, 10);*/

--Добавление записей для остатков товаров на складе 
/*INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (2, 1, 1, 2);
INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (3, 1, 2, 3);
INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (4, 1, 3, 4);
INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (5, 1, 4, 5);
INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (6, 1, 5, 6);
INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (7, 1, 6, 7);
INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (8, 1, 7, 8);
INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (9, 1, 8, 9);
INSERT INTO public.test_dev_product_stock(id, count_fact, count_reserv, link_dp_id) VALUES (10, 1, 9, 10);*/

--Добавление записей для спецификации документов
/*INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (2, 1, 2, 8000, 2, 2, 2, 2);
INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (3, 1, 2, 9000, 3, 3, 3, 3);
INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (4, 1, 2, 10000, 4, 4, 4, 4);
INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (5, 1, 2, 11000, 5, 5, 5, 5);
INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (6, 1, 2, 12000, 6, 6, 6, 6);
INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (7, 1, 2, 13000, 7, 7, 7, 7);
INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (8, 1, 2, 13000, 8, 8, 8, 8);
INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (9, 1, 2, 14000, 9, 9, 9, 9);
INSERT INTO public.test_dev_document_specification(id, counts, counts_reserv, price, discount, link_dh_id, link_dp_id, link_ps_id)
	VALUES (10, 1, 2, 15000, 10, 10, 10, 10);*/
