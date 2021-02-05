rule _Turbo_C_1987_naunwk
{
	meta:
		description = "Turbo C 1987"
	strings:
		$a = {FB8CCA2E8916????B430CD218B2E????8B1E????8EDA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
