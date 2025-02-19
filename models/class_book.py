class Livro:
    def __init__(self, id, titulo, autor, ano_publicacao, categoria, editora):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.categoria = categoria
        self.editora = editora
    
    # Método para retornar um dicionário com os atributos do objeto
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano_publicacao": self.ano_publicacao,
            "categoria": self.categoria,
            "editora": self.editora,
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], 
            data['titulo'], 
            data['autor'], 
            data['ano_publicacao'], 
            data['categoria'], 
            data['editora'], 
        )