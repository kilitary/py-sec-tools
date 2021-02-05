rule _Anskya_Binder_v1_1__Anskya_kblnzf
{
	meta:
		description = "Anskya Binder v1_1 __ Anskya"
	strings:
		$a = {BE??????0083C601FFE600000000????000000000000000000??????00??02????00100000000200}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
