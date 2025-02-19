
function InputForm({inputValue, onChange, onSubmit}) {

    return (
        <>
    
        <form className="input-form" onSubmit={onSubmit}>
          <input
            type="text"
            value={inputValue}
            onChange={onChange}
            placeholder="Type your question..."
          />
          <button> ➤ </button>
        </form>
    
        </>
      )

}

export default InputForm;