rule _Turbo_C_or_Borland_C__qkwfqo
{
	meta:
		description = "Turbo C or Borland C__"
	strings:
		$a = {BA????2E8916????B430CD218B2E????8B1E????8EDA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
