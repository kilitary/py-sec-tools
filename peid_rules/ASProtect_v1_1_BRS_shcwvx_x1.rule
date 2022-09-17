rule _ASProtect_v1_1_BRS_shcwvx
{
	meta:
		description = "ASProtect v1_1 BRS"
	strings:
		$a = {60E9??05}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
