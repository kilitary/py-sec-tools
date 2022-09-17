rule _ASProtect_v1_1_MTE_sgylsy
{
	meta:
		description = "ASProtect v1_1 MTE"
	strings:
		$a = {60E9????????9178797979E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
