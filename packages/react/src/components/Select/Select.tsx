import { forwardRef, type SelectHTMLAttributes } from 'react'
import { cn } from '../../utils'

export interface SelectProps extends SelectHTMLAttributes<HTMLSelectElement> {
  /** Select size */
  selectSize?: 'sm' | 'md' | 'lg'
}

export const Select = forwardRef<HTMLSelectElement, SelectProps>(
  ({ selectSize = 'md', className, children, ...props }, ref) => {
    return (
      <select
        ref={ref}
        className={cn(
          'void-select',
          selectSize !== 'md' && `void-select--${selectSize}`,
          className,
        )}
        {...props}
      >
        {children}
      </select>
    )
  }
)

Select.displayName = 'Select'
