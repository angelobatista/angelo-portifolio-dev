import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/produtos")
public class ProdutoController {
    private List<String> produtos = new ArrayList<>();

    @GetMapping
    public List<String> getProdutos() {
        return produtos;
    }

    @PostMapping
    public void addProduto(@RequestBody String produto) {
        produtos.add(produto);
    }
}
