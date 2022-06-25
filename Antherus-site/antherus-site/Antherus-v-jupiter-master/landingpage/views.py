from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Formulario, Perfil, CadastroClientes, Produto
from .forms import FormularioForm, StatusForm, AnotacoesForm, PerfilForm, CadastroClientesForm, ProdutoForm, \
    ContratacaoForm
from datetime import date, timedelta,datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.db.models import Q

import os


# Create your views here.

def index(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.status = "LEADS NOVO"
            post.data = datetime.now()
            post.save()
            return render(request, 'lp/agradecimento.html')
    else:
        form = FormularioForm()
    return render(request, 'lp/index.html', {'form': form})


def caixa_leads(request):
    # CAIXA LEADS
    cx_leads = reversed(Formulario.objects.all())
    form = Formulario.objects.all()
    # TOTAL DE LEADS
    contador = Formulario.objects.count()

    # PAGINATOR
    page = request.GET.get('page', 1)

    paginator = Paginator(form, 20)

    try:
        form = paginator.page(page)
    except PageNotAnInteger:
        form = paginator.page(1)
    except EmptyPage:
        form = paginator.page(paginator.num_pages)

    # FORM STATUS
    statu = StatusForm()

    # CONTAGEM  E LISTAGEM LEADS NOVOS
    count_novo = Formulario.objects.filter(status="LEADS NOVO").count()
    cx_leads_novos = reversed(Formulario.objects.filter(status="LEADS NOVO").all())

    # CONTAGEM E LISTAGEM lEADS POSITIVO
    count_leads_positivo = Formulario.objects.filter(status="LEADS POSITIVO").count()
    cx_leads_positivo = reversed(Formulario.objects.filter(status="LEADS POSITIVO").all())

    # CONTAGEM E LISTAGEM LEADS NEUTRO
    count_leads_neutro = Formulario.objects.filter(status="LEADS NEUTRO").count()
    cx_leads_neutro = reversed(Formulario.objects.filter(status="LEADS NEUTRO").all())

    # CONTAGEM LEADS NEGATIVO
    count_leads_negativo = Formulario.objects.filter(status="LEADS NEGATIVO").count()
    cx_leads_negativo = reversed(Formulario.objects.filter(status="LEADS NEGATIVO").all())

    total = Formulario.objects.count()

    # BLOCO DE ANOTAÇÕES
    bloco = AnotacoesForm()
    return render(request, 'lp/caixa-leads.html', {'form': form,
                                                   'cx_leads': cx_leads,
                                                   'cx_leads_novos': cx_leads_novos,
                                                   'cx_leads_positivo': cx_leads_positivo,
                                                   'cx_leads_neutro': cx_leads_neutro,
                                                   'cx_leads_negativo': cx_leads_negativo,
                                                   'statu': statu,
                                                   'bloco': bloco,
                                                   'contador': contador,
                                                   'count_leads_positivo': count_leads_positivo,
                                                   'count_leads_neutro': count_leads_neutro,
                                                   'count_leads_negativo': count_leads_negativo,
                                                   'count_novo': count_novo,
                                                   'total': total,
                                                   })


def leads(request, pk):
    open_leads = get_object_or_404(Formulario, pk=pk)
    # FORM STATUS
    sttus = StatusForm()
    notas = AnotacoesForm()
    # CONTAGEM  E LISTAGEM LEADS NOVOS
    count_novo = Formulario.objects.filter(status="LEADS NOVO").count()

    if request.method == "POST":
        my_file = request.POST.get('status')
        texto = request.POST.get('anotacoes')
        print(request.POST)
        if my_file is not None:
            Formulario.objects.filter(pk=pk).update(status=my_file)
        if texto is not None:
            Formulario.objects.filter(pk=pk).update(anotacoes=texto)
        print(open_leads.pk)
        return redirect(reverse('leads', args=[pk]))
    return render(request, 'lp/leads.html', {'open_leads': open_leads,
                                             'sttus': sttus,
                                             'notas': notas,
                                             'count_novo': count_novo,
                                             })


def status(request, pk):
    open_leads = get_object_or_404(Formulario, pk=pk)

    if request.method == "POST":
        my_file = request.POST.get('status')
        Formulario.objects.filter(pk=pk).update(status=my_file)
        print(open_leads.pk)
        return redirect('/dashboard')


def area_adm(request):
    print(request.POST)
    perfil = PerfilForm()
    display_perfil = Perfil.objects.all()

    # CONTAGEM  E LISTAGEM LEADS NOVOS
    count_novo = Formulario.objects.filter(status="LEADS NOVO").count()
    if request.method == "POST" and len(display_perfil) < 1:
        nome_pagina = request.POST.get("nome_pagina")
        n_whatsapp = request.POST.get("whatsapp")
        url_facebook = request.POST.get("perfil_facebook")
        url_instagram = request.POST.get("perfil_instagram")
        url_youtube = request.POST.get("canal_youtube")
        Perfil.objects.create(nome_pagina=nome_pagina,
                              whatsapp=n_whatsapp,
                              perfil_facebook=url_facebook,
                              perfil_instagram=url_instagram,
                              canal_youtube=url_youtube
                              )
        return HttpResponseRedirect('http://127.0.0.1:8000/area-adm/')
    else:
        if request.method == "POST" and len(display_perfil) == 1:
            nome_pagina = request.POST.get("nome_pagina")
            n_whatsapp = request.POST.get("whatsapp")
            url_facebook = request.POST.get("perfil_facebook")
            url_instagram = request.POST.get("perfil_instagram")
            url_youtube = request.POST.get("canal_youtube")
            Perfil.objects.update(nome_pagina=nome_pagina,
                                  whatsapp=n_whatsapp,
                                  perfil_facebook=url_facebook,
                                  perfil_instagram=url_instagram,
                                  canal_youtube=url_youtube
                                  )

            return HttpResponseRedirect('http://127.0.0.1:8000/area-adm/')
    return render(request, 'lp/area-administrativa.html', {'perfil': perfil,
                                                           'display_perfil': display_perfil,
                                                           'count_novo': count_novo,
                                                           })


def cadastro_produtos(request):
    if request.method == "POST":
        cad_produto = ProdutoForm(request.POST)
        if cad_produto.is_valid():
            produto = cad_produto.save(commit=False)
            produto.save()
            return redirect('lista-produtos')
    cad_produto = ProdutoForm()
    return render(request, 'lp/cadastro-produto.html', {'cad_produto': cad_produto})


def lista_produtos(request):
    produto_listado = Produto.objects.all()
    return render(request, 'lp/lista-de-produtos.html', {'produto_listado': produto_listado})


def editar_lista_produtos(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form_editar_produto = ProdutoForm(instance=produto)
    if request.method == "POST":
        produto_nome = request.POST.get('nome_produto')
        produto_descricao = request.POST.get('descricao')
        produto_valor = request.POST.get('valor')
        Produto.objects.update(nome_produto=produto_nome,
                               descricao=produto_descricao,
                               valor=produto_valor)
        return HttpResponseRedirect(reverse('lista-produtos'))
    else:
        return render(request, 'lp/editar-listagem-produtos.html', {'form_editar_produto': form_editar_produto,
                                                                    'produto': produto})


def deletar_produtos(request, pk):
    deletar_produto = get_object_or_404(Produto, pk=pk)
    deletar_produto.delete()
    return render(request, 'lp/produto-deletado.html')


def cadastro_clientes(request):
    cadastro = CadastroClientes.objects.all()

    if request.method == 'POST':
        tipo_juridico = request.POST.get("tipo_juridico")
        cnpj = request.POST.get("cnpj")
        nome_empresa = request.POST.get("nome_empresa")
        cpf = request.POST.get("cpf")
        nome_usuario = request.POST.get("nome_usuario")
        ramo_atividade = request.POST.get("ramo_atividade")
        telefone = request.POST.get("telefone")
        cep = request.POST.get("cep")
        endereco = request.POST.get("rua")
        num_endereco = request.POST.get("num-endereco")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("uf")
        status_cliente = request.POST.get("status_cliente")
        CadastroClientes.objects.create(tipo_juridico=tipo_juridico,
                                        cnpj=cnpj,
                                        nome_empresa=nome_empresa,
                                        cpf=cpf,
                                        nome_usuario=nome_usuario,
                                        ramo_atividade=ramo_atividade,
                                        telefone=telefone,
                                        cep=cep,
                                        endereco=endereco,
                                        num_endereco=num_endereco,
                                        bairro=bairro,
                                        cidade=cidade,
                                        estado=estado,
                                        status_cliente=status_cliente)

        return HttpResponseRedirect(reverse('lista-cliente'))
    else:
        form_clientes = CadastroClientesForm()
    return render(request, 'lp/cadastro-clientes.html', {'form_clientes': form_clientes})


def lista_clientes(request):
    # CONTAGEM  E LISTAGEM LEADS NOVOS
    count_novo = Formulario.objects.filter(status="LEADS NOVO").count()
    ficha_cliente = CadastroClientes.objects.all()
    busca = request.GET.get('search')
    print(busca)
    if busca:
        ficha_cliente = CadastroClientes.objects.filter(
            Q(tipo_juridico__icontains=busca) | Q(cnpj__icontains=busca) | Q(nome_empresa__icontains=busca) |
            Q(cpf__icontains=busca) | Q(nome_usuario__icontains=busca) | Q(ramo_atividade__icontains=busca) |
            Q(telefone__icontains=busca) | Q(cep__icontains=busca) | Q(endereco__icontains=busca) |
            Q(bairro__icontains=busca) | Q(cidade__icontains=busca) | Q(estado__icontains=busca)

        )
    return render(request, 'lp/lista-clientes.html', {'ficha_cliente': ficha_cliente,
                                                      'count_novo': count_novo})


def cliente_info(request, pk):
    ficha_cliente = get_object_or_404(CadastroClientes, pk=pk)
    perfil = Perfil()
    # Contador de Leads Novos
    count_novo = Formulario.objects.filter(status="LEADS NOVO").count()
    form_contrato = ContratacaoForm(request.POST)
    if request.method == "POST":
        form_contratacao = ContratacaoForm(request.POST, instance=ficha_cliente)
        if form_contratacao.is_valid():
            contrato = form_contratacao.save(commit=False)
            contrato.data_contratacao = date.today()
            contrato.data_vencimento = (date.today() + timedelta(30))
            contrato.save()
            pk = contrato.id
            return redirect(reverse('cliente', args=[pk]))
    else:
        return render(request, 'lp/cliente.html', {'ficha_cliente': ficha_cliente,
                                                   'perfil': perfil,
                                                   'count_novo': count_novo,
                                                   'form_contrato': form_contrato})


def editar_cliente(request, pk):
    # CONTAGEM   LISTAGEM LEADS NOVOS
    count_novo = Formulario.objects.filter(status="LEADS NOVO").count()
    post = get_object_or_404(CadastroClientes, pk=pk)
    form_clientes = CadastroClientesForm(instance=post)
    if request.method == 'POST':
        tipo_juridico = request.POST.get("tipo_juridico")
        cnpj = request.POST.get("cnpj")
        nome_empresa = request.POST.get("nome_empresa")
        cpf = request.POST.get("cpf")
        nome_usuario = request.POST.get("nome_usuario")
        ramo_atividade = request.POST.get("ramo_atividade")
        telefone = request.POST.get("telefone")
        cep = request.POST.get("cep")
        endereco = request.POST.get("rua")
        num_endereco = request.POST.get("num-endereco")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("uf")
        produto = request.POST.get("produto")
        CadastroClientes.objects.filter(pk=pk).update(tipo_juridico=tipo_juridico,
                                                      cnpj=cnpj,
                                                      nome_empresa=nome_empresa,
                                                      cpf=cpf,
                                                      nome_usuario=nome_usuario,
                                                      ramo_atividade=ramo_atividade,
                                                      telefone=telefone,
                                                      cep=cep,
                                                      endereco=endereco,
                                                      num_endereco=num_endereco,
                                                      bairro=bairro,
                                                      cidade=cidade,
                                                      estado=estado,
                                                      produto=produto)

        return HttpResponseRedirect(reverse('cliente', args=[pk]))

    form_clientes = CadastroClientesForm(instance=post)
    return render(request, 'lp/editar-cliente.html', {'form_clientes': form_clientes,
                                                      'post': post,
                                                      'count_novo': count_novo})


def deletar_cliente(request, pk):
    ficha_cliente = get_object_or_404(CadastroClientes, pk=pk)
    perfil = Perfil()
    print(request.method)
    if request.method == "POST":
        ficha_cliente.delete()
        return redirect(reverse('cliente-deletado'))
    return render(request, 'lp/deletar-cliente.html', {'ficha_cliente': ficha_cliente,
                                                       'perfil': perfil})


def cliente_deletado(request):
    print(request.method)
    if request.method == "GET":
        return redirect(reverse('lista-cliente'))
    return render(request, 'lp/cliente-deletado.html')
