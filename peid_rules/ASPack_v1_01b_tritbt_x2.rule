rule _ASPack_v1_01b_tritbt
{
	meta:
		description = "ASPack v1_01b"
	strings:
		$a = {60E8????????5D81EDCE3A44??B8C83A44??03C52B85B53E44??8985C13E44??80BDAC3E44}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
