DROP TABLE IF EXISTS USUARIO, TUTOR, CONTATO_EMERGENCIA, NOTIFICACAO, ENDERECO, HISTORICO_LOCALIZACAO, PET, AGENDAMENTO, CLINICA, TUTOR_CLINICA;

CREATE TABLE USUARIO(
	id_usuario char (9) PRIMARY KEY,
    nome varchar(30),
    email varchar(30),
    telefone char(11),
    senha varchar(20)
);

CREATE TABLE TUTOR(
	id_tutor char(9) PRIMARY KEY,
	inicio DATE,
    termino DATE
)

