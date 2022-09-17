rule _kryptor_9_shkfnr
{
	meta:
		description = "kryptor 9"
	strings:
		$a = {60E8????????5EB9????????2BC002040ED3C04979F8418D7E2C3346??66B9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
