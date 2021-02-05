rule _Turbo_C_zteuce
{
	meta:
		description = "Turbo C"
	strings:
		$a = {8CCA2E8916????B430CD218B2E????8B??????8EDAA3????8C06}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
