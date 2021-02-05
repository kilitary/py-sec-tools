rule _codeCrypter_0_31_plwpni
{
	meta:
		description = "codeCrypter 0_31"
	strings:
		$a = {5058535B90BB????4000FFE390CCCCCC558BEC5DC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
