rule _PRO_PACK_v2_08_xxuhdr
{
	meta:
		description = "PRO_PACK v2_08"
	strings:
		$a = {8CD38EC38CCA8EDA8B0E????8BF183????8BFED1??FDF3A553}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
