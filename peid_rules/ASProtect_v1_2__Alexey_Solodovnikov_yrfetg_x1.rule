rule _ASProtect_v1_2__Alexey_Solodovnikov_yrfetg
{
	meta:
		description = "ASProtect v1_2 __ Alexey Solodovnikov"
	strings:
		$a = {9060E81B000000E9FC8DB50F0600008BFEB997000000AD3578563412AB4975F6EB045D4555C3E9??????00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
