DROP TABLE IF EXISTS USUARIO, TUTOR, CONTATO_EMERGENCIA, NOTIFICACAO, ENDERECO, HISTORICO_LOCALIZACAO, PET,
AGENDAMENTO, CLINICA, TUTOR_CLINICA;

CREATE TABLE USUARIO(
	id_usuario 	char 	(9) 	PRIMARY KEY,
    nome 		varchar	(30)	NOT NULL,
    email 		varchar	(30)	NOT NULL,
    telefone 	char	(11)	NOT NULL,
    senha 		varchar	(20)	NOT NULL
);

CREATE TABLE TUTOR(
	id_pessoa 	char	(9) 	PRIMARY KEY,
    id_tutor	char	(9)		UNIQUE NOT NULL,	
    FOREIGN KEY (id_pessoa) REFERENCES USUARIO(id_usuario) ON DELETE CASCADE -- CASO USUARIO SEJA EXCLUIDO O TUTOR TAMBÉM SOME DO BANCO
);

CREATE TABLE CONTATO_EMERGENCIA(
	id_pessoa 	char	(9) 	PRIMARY KEY,
    id_contato	char	(9)		UNIQUE NOT NULL,	
	id_tutor	char	(9)		NOT NULL,
    parentesco 	enum	('Pai', 'Mãe', 'Filho(a)', 'Amigo(a)', 'Cônjuge', 'Outros')	NOT NULL,
    FOREIGN KEY (id_pessoa) REFERENCES USUARIO(id_usuario) 	ON DELETE CASCADE,
    FOREIGN KEY (id_tutor) 	REFERENCES TUTOR(id_tutor)		ON DELETE CASCADE -- CASO USUARIO OU TUTOR RELACIONADO SEJA APAGADO SOME DO BANCO
);

CREATE TABLE HISTORICO_LOCALIZACAO(
	id_coleira 	char	(9) 	PRIMARY KEY,
	latitude	float	(8),
    longitude	float	(8),
    FOREIGN KEY (id_coleira) REFERENCES PET(id_coleira)		ON DELETE CASCADE
);



-- 1. Cria um usuário que será o Tutor
INSERT INTO USUARIO (id_usuario, nome, email, telefone, senha) 
VALUES ('123456789', 'Ana Souza', 'ana@email.com', '11988887777', 'senha123');

-- 2. Torna esse usuário um Tutor
INSERT INTO TUTOR (id_pessoa, id_tutor) 
VALUES ('123456789', 'TUT001');

-- 3. Cria um segundo usuário que será o Contato de Emergência
INSERT INTO USUARIO (id_usuario, nome, email, telefone, senha) 
VALUES ('987654321', 'Carlos Silva', 'carlos@email.com', '11977778888', 'senha456');

-- 4. Cadastra o contato de emergência vinculado ao tutor
INSERT INTO CONTATO_EMERGENCIA (id_pessoa, id_contato, id_tutor, parentesco) 
VALUES ('987654321', 'CONT001', 'TUT001', 'Amigo(a)');
