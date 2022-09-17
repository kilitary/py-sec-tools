rule _fasm__Tomasz_Grysztar_unnngk
{
	meta:
		description = "fasm __ Tomasz Grysztar"
	strings:
		$a = {5355568B74241485F657B801000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
