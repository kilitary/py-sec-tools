rule _yoda_s_Protector_1_02__1_03__Ashkbiz_Danehkar_rxlqpt
{
	meta:
		description = "yoda_s Protector 1_02 _ 1_03 __ Ashkbiz Danehkar"
	strings:
		$a = {E803000000EB01??BB55000000E803000000EB01??E88F000000E803000000EB01??E882000000E803000000EB01??E8B8000000E803000000EB01??E8AB0000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
