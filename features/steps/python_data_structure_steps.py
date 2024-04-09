from behave import given, when, then, step, fixture

list1 = None
list2 = None
list1_filter = None
list2_filter = None
result = []


@given(u'I have the following lists')
def step_impl(context):
    global list1, list2
    for row in context.table:
        print(f'{row["collection"]}')
    list1, list2 = context.table
    list1 = list1["collection"].split(',')
    list2 = list2["collection"].split(',')


@when(u'I ask python to use the strategy')
def step_impl(context):
    global list1_filter, list2_filter
    for row in context.table:
        print(f'{row["list"]} - {row["type"]}')
    list1_filter = context.table[0]["type"]
    list2_filter = context.table[1]["type"]


@then(u'python should give me the result')
def step_impl(context):
    global result
    print(context.text.rstrip().lstrip().split(','))
    if list1_filter=='odd':
        result.extend(list1[1::2])
    else:
        result.extend(list1[0::2])
    if list2_filter=='odd':
        result.extend(list2[1::2])
    else:
        result.extend(list2[0::2])
    print(result)
    assert result == context.text.rstrip().lstrip().split(',')
