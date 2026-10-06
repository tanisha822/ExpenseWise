from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Budget
from django.db.models import Sum, Avg
from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url='login')
def home_view(request):

    if request.method == "POST":

        title = request.POST["title"]
        amount = request.POST["amount"]
        category = request.POST["category"]
        date = request.POST["date"]
        description = request.POST["description"]

        Expense.objects.create(
            user=request.user,
            title=title,
            amount=amount,
            category=category,
            date=date,
            description=description
        )

        return redirect("home")

    search = request.GET.get("search", "")
    category = request.GET.get("category", "")
    start_date = request.GET.get("start_date", "")
    end_date = request.GET.get("end_date", "")

    expenses = Expense.objects.filter(user=request.user)

    if search:
        expenses = expenses.filter(title__icontains=search)

    if category:
        expenses = expenses.filter(category__iexact=category)

    if start_date:
        expenses = expenses.filter(date__gte=start_date)

    if end_date:
        expenses = expenses.filter(date__lte=end_date)

    total_expenses = expenses.aggregate(
        Sum("amount")
    )["amount__sum"] or 0

    expense_count = expenses.count()

    average_expense = expenses.aggregate(
        Avg("amount")
    )["amount__avg"] or 0

    categories = Expense.objects.filter(
        user=request.user
    ).values_list(
        "category",
        flat=True
    ).distinct()

    monthly_expenses = (
        Expense.objects
        .filter(user=request.user)
        .annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("-month")
    )

    category_expenses = (
        Expense.objects
        .filter(user=request.user)
        .values("category")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )

    current_month = timezone.now().date().replace(day=1)

    budget = Budget.objects.filter(
        user=request.user,
        month=current_month
    ).first()

    monthly_spent = Expense.objects.filter(
        user=request.user,
        date__year=current_month.year,
        date__month=current_month.month
    ).aggregate(
        Sum("amount")
    )["amount__sum"] or 0

    remaining_budget = 0
    budget_percentage = 0
    budget_status = "No Budget Set"

    if budget:

        remaining_budget = budget.amount - monthly_spent

        if remaining_budget < 0:
            remaining_budget = 0

        if budget.amount > 0:

            budget_percentage = (
                monthly_spent / budget.amount
            ) * 100

        if budget_percentage >= 100:
            budget_percentage = 100
            budget_status = "Budget Exceeded"

        elif budget_percentage >= 80:
            budget_status = "Budget Almost Reached"

        else:
            budget_status = "Within Budget"

    context = {
        "expenses": expenses,
        "total_expenses": total_expenses,
        "expense_count": expense_count,
        "average_expense": average_expense,
        "search": search,
        "category": category,
        "categories": categories,
        "start_date": start_date,
        "end_date": end_date,
        "monthly_expenses": monthly_expenses,
        "category_expenses": category_expenses,
        "budget": budget,
        "monthly_spent": monthly_spent,
        "remaining_budget": remaining_budget,
        "budget_percentage": budget_percentage,
        "budget_status": budget_status
    }

    return render(
        request,
        "expenses/home.html",
        context
    )


@login_required(login_url='login')
def add_budget_view(request):

    if request.method == "POST":

        amount = request.POST["amount"]

        if float(amount) <= 0:
            return redirect("home")

        current_month = timezone.now().date().replace(day=1)

        Budget.objects.update_or_create(
            user=request.user,
            month=current_month,
            defaults={
                "amount": amount
            }
        )

        return redirect("home")

    return redirect("home")


@login_required(login_url='login')
def edit_expense(request, id):

    expense = get_object_or_404(
        Expense,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        expense.title = request.POST["title"]
        expense.amount = request.POST["amount"]
        expense.category = request.POST["category"]
        expense.date = request.POST["date"]
        expense.description = request.POST["description"]

        expense.save()

        return redirect("home")

    return render(
        request,
        "expenses/edit_expense.html",
        {"expense": expense}
    )


@login_required(login_url='login')
def delete_expense(request, id):

    expense = get_object_or_404(
        Expense,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        expense.delete()

    return redirect("home")