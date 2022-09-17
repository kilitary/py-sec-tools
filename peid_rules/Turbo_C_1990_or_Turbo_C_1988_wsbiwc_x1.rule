rule _Turbo_C_1990_or_Turbo_C_1988_wsbiwc
{
	meta:
		description = "Turbo C 1990 or Turbo C 1988"
	strings:
		$a = {BA????2E89??????B430CD218B??????8B??????8EDA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
