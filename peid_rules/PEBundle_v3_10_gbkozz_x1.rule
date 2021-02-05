rule _PEBundle_v3_10_gbkozz
{
	meta:
		description = "PEBundle v3_10"
	strings:
		$a = {9C60E80200000033C08BC483C004938BE38B5BFC81EB0720400087DD????????400001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
